import cv2
import time
import numpy as np

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_GAMMA, 3.25)
cam.set(cv2.CAP_PROP_EXPOSURE, 30600)
cam.set(cv2.CAP_PROP_EXPOSURE,-5)
cam.set(cv2.CAP_PROP_GAIN, 10)
w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)



'''
### 실시간 영상 출력
i = 0
while 1:


    ret, frame = cam.read()

    cv2.imshow("VideoFrame", frame)
    cv2.imwrite("./ifi/{}.jpg".format(i), frame)
    if cv2.waitKey(1) > 0: break
    print(np.max(frame))
    i +=1
'''

### 이미지 5개 받아오기
### 전처리 (OPD) 한후 -> R,G,B, gray 나누고 각각 5장씩
### R,G,B, gray 4개

img_list = []

for i in range(5):
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./ifi/{}.jpg".format(i), gray)

    img_list.append(gray)

print(len(img_list))


cam.release()
cv2.destroyAllWindows()