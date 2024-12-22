import numpy as np
import openvino as ov
import matplotlib.pyplot as plt
import cv2

core = ov.Core()

# 얼굴 인식 모델
model_face = core.read_model(model='./model/face-detection-adas-0001.xml')
compiled_model_face = core.compile_model(model = model_face, device_name="CPU")

input_layer_face = compiled_model_face.input(0)
output_layer_face = compiled_model_face.output(0)

#감정 인식 모델
model_emo = core.read_model(model='./model/emotions-recognition-retail-0003.xml')
compiled_model_emo = core.compile_model(model = model_emo, device_name="CPU")

input_layer_emo = compiled_model_emo.input(0)
output_layer_emo = compiled_model_emo.output(0)

# 나이, 성별 인식 모델
model_ag = core.read_model(model='./model/age-gender-recognition-retail-0013.xml')
compiled_model_ag = core.compile_model(model = model_ag, device_name="CPU")

input_layer_ag = compiled_model_ag.input(0)
output_layer_ag = compiled_model_ag.output

def preprocess(image, input_layer_face):
	N, input_channels, input_height, input_width = input_layer_face.shape

	resized_image = cv2.resize(image, (input_width, input_height))
	transposed_image = resized_image.transpose(2, 0, 1)
	input_image = np. expand_dims(transposed_image, 0)

	return input_image

def find_faceboxes(image, results, confidence_threshold):
	results = results.squeeze()
	
	scores = results[:,2]
	boxes = results[:, -4:]

	face_boxes = boxes[scores >= confidence_threshold]
	scores = scores[scores >= confidence_threshold]

	image_h, image_w, image_channels = image.shape
	face_boxes = face_boxes*np.array([image_w, image_h, image_w, image_h])
	face_boxes = face_boxes.astype(np.int64)

	return face_boxes, scores

def draw_faceboxes(image, face_boxes, scores):

	show_image = image.copy()

	for i in range(len(face_boxes)):
		
		xmin, ymin, xmax, ymax = face_boxes[i]
		cv2.rectangle(img=show_image, pt1=(xmin,ymin), pt2=(xmax,ymax), color=(0,200,0), thickness=2)

	return show_image

def draw_emotions(face_boxes, image, show_image):
    EMOTION_NAMES = ['neutral', 'happy', 'sad', 'surprise', 'anger']
    emotion_indexes = []  # index 값을 저장할 리스트 추가

    for i in range(len(face_boxes)):
        xmin, ymin, xmax, ymax = face_boxes[i]
        face = image[ymin:ymax, xmin:xmax]

        input_image = preprocess(face, input_layer_emo)
        results_emo = compiled_model_emo([input_image])[output_layer_emo]

        results_emo = results_emo.squeeze()
        index = np.argmax(results_emo)
        emotion_indexes.append(index)  # index 값을 리스트에 추가

        text = EMOTION_NAMES[index]
        cv2.putText(show_image, text, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 200, 0), 2)

    return emotion_indexes  # 감정 인식의 index 값을 반환

def draw_age_gender(face_boxes, image):
    EMOTION_NAMES = ['neutral', 'happy', 'sad', 'surprise', 'anger']
    show_image = image.copy()
    emotion_indexes = []  # index 값을 저장할 리스트 추가
    for i in range(len(face_boxes)):
        xmin, ymin, xmax, ymax = face_boxes[i]
        xmin = max(0, xmin)
        ymin = max(0, ymin)
        xmax = min(image.shape[1], xmax)
        ymax = min(image.shape[0], ymax)
        face = image[ymin:ymax, xmin:xmax]

        # --- emotion ---
        input_image = preprocess(face, input_layer_emo)
        results_emo = compiled_model_emo([input_image])[output_layer_emo]
        results_emo = results_emo.squeeze()
        index = np.argmax(results_emo)
        if index >= len(EMOTION_NAMES):
            index = 0
        emotion_indexes.append(EMOTION_NAMES[index])  # index 값을 리스트에 추가
        
        # --- age and gender ---
        input_image_ag = preprocess(face, input_layer_ag)
        results_ag = compiled_model_ag([input_image_ag])
        age, gender = results_ag[1], results_ag[0]
        age = np.squeeze(age)
        age = int(age * 100)
        box_color = (255, 255, 255)
        gender = np.squeeze(gender)
        fontScale = max(0.5, image.shape[1] / 750)
        text = f"{EMOTION_NAMES[index]}"
        cv2.putText(show_image, text, (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 200, 0), 2)
        cv2.rectangle(show_image, (xmin, ymin), (xmax, ymax), box_color, 2)

    return show_image, emotion_indexes

def predict_image(image, conf_threshold):
    input_image = preprocess(image, input_layer_face)
    results = compiled_model_face([input_image])[output_layer_face]
    face_boxes, scores = find_faceboxes(image, results, conf_threshold)
    visualize_image = draw_age_gender(face_boxes, image)

    return visualize_image
