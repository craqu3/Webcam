'''
Programmer.: (C) craqu3
Date.......: 05/02/2025
Observation: Program for activate webcam with OpenCV.
'''

import cv2 as cv
import time

cam = int(input("[1] - Original Image - No effects\n[2] - Gray Image\n[3] - Canny Image\n[4] - Blur Image\n[5] - Black and White Image\n\n Enter a number:"))

list = [1,2,3,4,5]

if cam in list:
    print("Wait the window is opening...")
else:
    print("U need to enter a number 1 - 5")
    time.sleep(2.5)
    exit()

webcam = cv.VideoCapture(0)

if not webcam:
    print("No webcam found")


while True:
    returning, frame = webcam.read()
    if not returning:
        print("Error")
        break
    frameBlur = cv.blur(frame, (15,15))
    frameCanny = cv.Canny(frame, 100, 200)
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (status, framePB) = cv.threshold(frameGray, 127, 255, cv.THRESH_BINARY)

    if cam == 1:
        cv.imshow('Original Image', frame)
    elif cam == 2:
        cv.imshow('Gray Image', frameGray)
    elif cam == 3:
        cv.imshow('Canny Image', frameCanny)
    elif cam == 4:
        cv.imshow('Blur Image', frameBlur)
    elif cam == 5:
        cv.imshow('Black and white Image', framePB)
    else:
        print("Error on input")

    if cv.waitKey(1) == ord('esc'):
        break

webcam.release()
cv.destroyAllWindows()