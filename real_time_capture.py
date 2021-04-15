import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
import imutils
import os
import streamlit as st
import time
import json
#--------------------------------------------
# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Fine', 'X', 'hello']


def app():
    def log_in(messages):
        with open('log/app.log', 'a') as f:
            f.write(f'{messages}\n')

    with open('messages/symbol_to_text.json') as f:
        ALPHABET = json.load(f)
    log_in(f'{ALPHABET}')
    model = tf.keras.models.load_model("saved_models/sign_language")

    def classify(image):
        image = cv2.resize(image, (28, 28))
        image = image.astype("float") / 255.0
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        proba = model.predict(image)
        idx = np.argmax(proba)
        log_in(f'{type(idx)} {idx}')
        log_in(f'{ALPHABET}')

        return ALPHABET[str(idx.item())]

    st.title("Webcam Live Feed")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    FRAME_WINDOW_3 = st.image([])

    st.sidebar.title('Sign Language Detection')

    st.sidebar.markdown("### Symbols For Ref!")
    image = cv2.imread('Datasets/amer_sign2.png')
    # banner = cv2.imread('Datasets/banner.png')
    st.sidebar.image(image)
    st.sidebar.markdown("### ROI Hand!")

    FRAME_WINDOW_2 = st.sidebar.image([])

    cap = cv2.VideoCapture(0)

    last_seen = None
    seen_count = 0
    while run:
        ret, img = cap.read()
        banner = cv2.imread('Datasets/banner.png')
        img = cv2.flip(img, 1)
        top, right, bottom, left = 75, 350, 300, 590
        roi = img[top:bottom, right:left]
        roi = cv2.flip(roi, 1)
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        # cv2.imshow('roi', gray)
        # with second:

        FRAME_WINDOW_2.image(gray)

        alpha = classify(gray)
        # st.sidebar.markdown(alpha)
        cv2.rectangle(img, (left, top), (right, bottom), (255, 255, 255), 3)
        font = cv2.FONT_HERSHEY_SIMPLEX

        if alpha != last_seen:
            last_seen = alpha
            seen_count = 0
        elif alpha == last_seen:
            seen_count += 1
        if seen_count >= 3:
            cv2.putText(banner, alpha, (0, 130), font, 3, (0, 0, 255), 2)
        # cv2.resize(img,(1000,1000))
        # cv2.imshow('img', img)
        FRAME_WINDOW.image(img)
        FRAME_WINDOW_3.image(banner)
        # time.sleep(0.1)
    else:
        st.write('Stopped')
        cap.release()

    # key = cv2.waitKey(1) & 0xFF
    # if key == ord('q'):
    #     break
# cap.release()
# cv2.destroyAllWindows()
