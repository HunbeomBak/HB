import numpy as np
import cv2
import matplotlib.pyplot as plt
import nidaqmx

def Init():
    a = []
    b = []
    c = []
    d = []

    return a,b,c,d

def Cam_setting(cam):
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_GAMMA, 3.25)
    cam.set(cv2.CAP_PROP_EXPOSURE, 30600)
    cam.set(cv2.CAP_PROP_EXPOSURE, -5)
    cam.set(cv2.CAP_PROP_GAIN, 10)



def Move(voltage):
    pass


def OPD():
    pass


#카메라 지정
camera = cv2.VideoCapture('./data/20190911_4 max.avi')
n_frame = camera.get(cv2.CAP_PROP_FRAME_COUNT)
w,h = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

center = (int(h/2),int(w/2))
print(center)


#카메라 설정
#Cam_setting(camera)

# 이미지 넣을 리스트 만듦
Gray_list, B_list ,G_list ,R_list  = Init()
Gray_I, B_I,G_I,R_I = Init()

A =[]
a = range(int(n_frame))

#사진 20번찍으면서 각각 리스트에 넣음
for i in a:
    rec, frame = camera.read()

    B,G,R = frame[:,:,0], frame[:,:,1], frame[:,:,2]
    B_list.append(B)
    B_I.append(B[center])

    G_list.append(G)
    G_I.append(G[center])

    R_list.append(R)
    R_I.append(R[center])

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Gray_list.append(gray)

    cv2.imshow('test', gray)
    #cv2.waitKey(10)

    print(i)  # 몇번째 루프인지 출력

    #Move() #PZT 움직일 함수
    #OPD() # OPD 전처리

camera.release()

print("촬영 종료")

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(a, B_I, 'b') # 5 points tolerance
line, = ax.plot(a, B_I, 'o', picker=5)  # 5 points tolerance



def onpick(event):
    global B_I, A

    if event.artist!=line: return True

    N = len(event.ind)
    if not N: return True

    i = event.ind[0]
    A = [B_I[i],B_I[i+1],B_I[i+2],B_I[i+3],B_I[i+4]]
    print(A)

fig.canvas.mpl_connect('pick_event', onpick)


plt.show()
