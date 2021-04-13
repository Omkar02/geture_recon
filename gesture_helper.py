import cv2
import numpy as np
from matplotlib import pyplot as plt
import time


def get_firstFrame():
    cap = cv2.VideoCapture(0)
    ret, firstFrame = cap.read()
    gray = cv2.cvtColor(firstFrame, cv2.COLOR_BGR2GRAY)
    cap.release()
    print('done')
    time.sleep(1)
    cv2.imshow('frame', gray)
    cv2.destroyAllWindows()
    return gray


def capture_training_images(gesture_name):
    save_file_path = '/custom_gesture_images'
    firstFrame = get_firstFrame()
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray, (5, 5), 0)
        frameDelta = cv2.absdiff(firstFrame, gray)
        # ret, th1 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        # Display the resulting frame
        cv2.imshow('frame', frameDelta)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


capture_training_images('hi')
