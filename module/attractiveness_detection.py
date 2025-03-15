from keras.models import load_model
from keras.optimizers import SGD
from mtcnn.mtcnn import MTCNN
import streamlit as st
from PIL import Image
import numpy as np
import tempfile
import cv2

ATTRACTIVENESS_THRESHOLD = 0.5


class AttractivenessModel:
    def __init__(self, model_path):
        self.model = load_model(model_path, compile=False)
        self.model.compile(optimizer=SGD(learning_rate=0.0001, momentum=0.9), loss='categorical_crossentropy')

    def preprocess_face(self, face):
        face = cv2.resize(cv2.cvtColor(face, cv2.COLOR_BGR2RGB), (178, 218))
        face = face.astype(np.float32) / 255.0
        face = np.expand_dims(face, axis=0)
        return face

    def predict(self, face):
        processed_face = self.preprocess_face(face)
        prediction = self.model.predict(processed_face)[0][0]
        return prediction


class FaceDetector:
    def __init__(self):
        self.detector = MTCNN()

    def detect_faces(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = self.detector.detect_faces(rgb_frame)
        return faces


class FaceAttractivenessApp:
    def __init__(self, model_path):
        self.model = AttractivenessModel(model_path)
        self.detector = FaceDetector()

    def draw_faces(self, frame, faces):
        for result in faces:
            x, y, width, height = result['box']
            face = frame[y:y + height, x:x + width]

            if face.size != 0:
                prediction = self.model.predict(face)

                color = (0, 255, 0) if prediction >= ATTRACTIVENESS_THRESHOLD else (0, 0, 255)
                label = f'Attractive: {prediction:.2f}' if prediction >= ATTRACTIVENESS_THRESHOLD else f'Not Attractive: {prediction:.2f}'

                cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        return frame

    def process_image(self, image):
        image = Image.open(image)
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        faces = self.detector.detect_faces(frame)

        frame = self.draw_faces(frame, faces)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.image(frame, channels="RGB", use_container_width=True)

    def process_video(self, video):
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            faces = self.detector.detect_faces(frame)
            frame = self.draw_faces(frame, faces)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB", use_container_width=True)

        cap.release()

    def process_camera(self):
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Camera not available!", icon="🔴")
                break

            faces = self.detector.detect_faces(frame)
            frame = self.draw_faces(frame, faces)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame, channels="RGB", use_container_width=True)

        cap.release()

