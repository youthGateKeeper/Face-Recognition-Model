import numpy as np
import openvino as ov
import matplotlib.pyplot as plt
import cv2
import csv
core = ov.Core()
model_face = core.read_model(model='./model/face-detection-adas-0001.xml')
compiled_model_face = core.compile_model(model = model_face, device_name="CPU")
input_layer_face = compiled_model_face.input(0)
output_layer_face = compiled_model_face.output(0)
model_emo = core.read_model(model='./model/emotions-recognition-retail-0003.xml')
compiled_model_emo = core.compile_model(model = model_emo, device_name="CPU")
input_layer_emo = compiled_model_emo.input(0)
output_layer_emo = compiled_model_emo.output(0)
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
    for i in range(len(face_boxes)):
        xmin, ymin, xmax, ymax = face_boxes[i]
        face = image[ymin:ymax, xmin:xmax]
        input_image = preprocess(face, input_layer_emo)
        results_emo = compiled_model_emo([input_image])[output_layer_emo]
        results_emo = results_emo.squeeze()
        index = np.argmax(results_emo)
        text = EMOTION_NAMES[index]
        cv2.putText(show_image, text, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 200, 0), 2)
def draw_age_gender(face_boxes, image):
    EMOTION_NAMES = ['neutral', 'happy', 'sad', 'surprise', 'anger']
    show_image = image.copy()
    for i in range(len(face_boxes)):
        xmin, ymin, xmax, ymax = face_boxes[i]
        xmin = max(0, xmin)
        ymin = max(0, ymin)
        xmax = min(image.shape[1], xmax)
        ymax = min(image.shape[0], ymax)
        face = image[ymin:ymax, xmin:xmax]
        input_image = preprocess(face, input_layer_emo)
        results_emo = compiled_model_emo([input_image])[output_layer_emo]
        results_emo = results_emo.squeeze()
        index = np.argmax(results_emo)
        total_data.append(results_emo)
        if index >= len(EMOTION_NAMES):
            index = 0
        input_image_ag = preprocess(face, input_layer_ag)
        results_ag = compiled_model_ag([input_image_ag])
        age, gender = results_ag[1], results_ag[0]
        age = np.squeeze(age)
        age = int(age * 100)
        gender = np.squeeze(gender)
        fontScale = max(0.5, image.shape[1] / 750)
        text = f"{EMOTION_NAMES[index]}"
        cv2.putText(show_image, text, (xmin, ymin - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 200, 0), 2)
        cv2.rectangle(show_image, (xmin, ymin), (xmax, ymax), box_color, 2)
        if (len(total_data) >= 1000):
            import csv
            import os
            now = dt.datetime.now()
            try:
                if (csv_name == None or csv_name == ""):
                    csv_name = now.strftime('20%y_%m_%d_%H_%M_%S_1000')
            except:
                csv_name = now.strftime('20%y_%m_%d_%H_%M_%S')
            single_data = []
            Multiple_data = [['neutral', 'happy', 'sad', 'surprise', 'anger']]
            columns = ['neutral', 'happy', 'sad', 'surprise', 'anger']
            for i in range(len(total_data)):
                for j in range(5):
                    single_data.append(total_data[i][j])
                for a in range(5):
                    Multiple_data[i].append(single_data[i])
                Multiple_data.append([])
            f = open(f"{csv_name}.csv", "w")
            writer = csv.writer(f)
            writer.writerows(Multiple_data)
            f.close()
            time.sleep(2)
            import pandas as pd
            df = pd.read_csv(f'{csv_name}.csv')
            df = df.drop(index=range(5, 10))
            time.sleep(2)
            import csv
            f = open(f"{csv_name}.csv", "r")
            reader = csv.reader(f)
            #for row in reader:
                #print(row)
            single_data = csv.reader(f)
            print(single_data)
    return show_image
def predict_image(image, conf_threshold):
    input_image = preprocess(image, input_layer_face)
    results = compiled_model_face([input_image])[output_layer_face]
    face_boxes, scores = find_faceboxes(image, results, conf_threshold)
    visualize_image = draw_age_gender(face_boxes, image)
    return visualize_image