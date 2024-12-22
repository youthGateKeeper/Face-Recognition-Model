# app.py 수정
import streamlit as st
import cv2
import PIL
from PIL import Image
import numpy
import utils
import io
import time
import google.generativeai as genai 

st.sidebar.header("Setting")
conf_threshold = float(st.sidebar.slider("Select the Confidence Threshold", 10, 100, 20)) / 100
my_api_key = "AIzaSyDU7O5ZFRDVYtBYjP-zPU2FPXL44qN14ys"
genai.configure(api_key=my_api_key)

@st.cache_resource
def load_model():
    model = genai.GenerativeModel('gemini-pro')
    return model

model = load_model()

st.sidebar.header("Needed Help?")
with st.sidebar:
    if "chat_session" not in st.session_state:
        st.session_state["chat_session"] = model.start_chat(history=[]) 
    for content in st.session_state.chat_session.history:
        with st.chat_message("ai" if content.role == "model" else "user"):
            st.markdown(content.parts[0].text)
    if prompt := st.chat_input("메시지를 입력하세요."):
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("ai"):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)

def play_video(video_source):
    camera = cv2.VideoCapture(video_source)
    st_frame = st.empty()
    emotion_index_placeholder = st.empty()

    while(camera.isOpened()):
        ret, frame = camera.read()
        if ret:
            visualized_image, emotion_indexes = utils.predict_image(frame, conf_threshold)
            st_frame.image(visualized_image, channels="BGR")
            emotion_index_placeholder.text(emotion_indexes[0])
        else:
            camera.release()
            break

basic_radio = st.sidebar.radio("Select", ["Data Collection", "Utilize_collected_data"])

if basic_radio == "Utilize_collected_data":
    source_radio = st.sidebar.radio("Select Source", ["IMAGE", "VIDEO", "WEBCAM"])
    input = None
    if source_radio == "IMAGE":
        st.sidebar.header("Upload")
        input = st.sidebar.file_uploader("Choose an image.", type=("jpg", "png"))
        if input is not None:
            uploaded_image = PIL.Image.open(input)
            uploaded_image_cv = cv2.cvtColor(numpy.array(uploaded_image), cv2.COLOR_RGB2BGR)
            visualized_image, emotion_indexes = utils.predict_image(uploaded_image_cv, conf_threshold=conf_threshold)
            st.image(visualized_image, channels="BGR")
            st.text(emotion_indexes[0])
    temporary_location = None

    if source_radio == "VIDEO":
        st.sidebar.header("Upload")
        input = st.sidebar.file_uploader("Choose a video.", type=("mp4"))
        if input is not None:
            g = io.BytesIO(input.read())
            temporary_location = "upload.mp4"
            with open(temporary_location, "wb") as out:
                out.write(g.read())
            out.close()
        if temporary_location is not None:
            play_video(temporary_location)
            if st.button("Replay", type="primary"):
                pass
    if source_radio == "WEBCAM":
        play_video(0)
else:
    import Collection
    source_radio = st.sidebar.radio("Select Source", ["IMAGE", "VIDEO", "WEBCAM"])
    input = None
    if source_radio == "IMAGE":
        st.sidebar.header("Upload")
        input = st.sidebar.file_uploader("Choose an image.", type=("jpg", "png"))
        if input is not None:
            uploaded_image = PIL.Image.open(input)
            uploaded_image_cv = cv2.cvtColor(numpy.array(uploaded_image), cv2.COLOR_RGB2BGR)
            visualized_image, emotion_indexes = utils.predict_image(uploaded_image_cv, conf_threshold=conf_threshold)
            st.image(visualized_image, channels="BGR")
            st.text(emotion_indexes[0])
    temporary_location = None

    if source_radio == "VIDEO":
        st.sidebar.header("Upload")
        input = st.sidebar.file_uploader("Choose a video.", type=("mp4"))
        if input is not None:
            g = io.BytesIO(input.read())
            temporary_location = "upload.mp4"
            with open(temporary_location, "wb") as out:
                out.write(g.read())
            out.close()
        if temporary_location is not None:
            play_video(temporary_location)
            if st.button("Replay", type="primary"):
                pass
    if source_radio == "WEBCAM":
        play_video(0)
