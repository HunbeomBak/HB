import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

class Anessa:

    def __init__(self):
        self.x = []
        self.y = []
        self.i = 0

        self.r = 0
        self.c = 0

        self.Road_Video()
        self.Run()
        self.Plot()

    def Get_input(self):
        self.r = input("몇번째 row? (자연수만 입력) :")
        self.c = input("몇번째 colom? (자연수만 입력) :")

    def Road_Video(self):
        self.cap = cv2.VideoCapture('test4 max.avi')

        nf = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 프레임 수
        print(nf)

    def Run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                point = np.mean(frame[527][635])
                print(point)

                self.y.append(point)
                self.x.append(self.i)

                self.i += 1

            else:
                break

    def Plot(self):
        plt.plot(self.x, self.y)
        plt.xlabel("number of frame")
        plt.ylabel("Intensity")
        plt.show()

A = Anessa()
