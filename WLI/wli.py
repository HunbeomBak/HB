import numpy as np
import cv2
import nidaqmx

def Cam_setting(cam):
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_GAMMA, 3.25)
    cam.set(cv2.CAP_PROP_EXPOSURE, 30600)
    cam.set(cv2.CAP_PROP_EXPOSURE, -5)
    cam.set(cv2.CAP_PROP_GAIN, 10)


def Get_cam(camera):
    rec, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return frame

def Move():
    pass


def OPD():
    pass



camera = cv2.VideoCapture(0)

Cam_setting(camera)


image_list = []

for i in range(4):

    gray = Get_cam(camera)

    image_list.append(gray)

    Move()
    OPD()

    print(i)

print(len(image_list))

cv2.imshow('test',image_list[3])
cv2.waitKey(0)

camera.release()
