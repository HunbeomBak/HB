import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

class Anessa:

    def __init__(self):
        self.x = []

        self.center_b = [] #Blue
        self.center_g = [] #Green
        self.center_r = [] #Red

        self.side_b = []
        self.side_g = []
        self.side_r = []

        self.frames = []

        self.i = 1

        self.Road_Video()
        self.Run()
        self.Plot()


    def Road_Video(self):
        self.cap = cv2.VideoCapture('./data/20190917.avi')

        self.nf = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 프레임 수
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.num_pixel = width * height
        print(self.nf)

    def Run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:

                if self.i % 10 ==0:
                    center = (np.shape(frame)[0:2])
                    print(center)
                    point_center = frame[520][696] # 가운데
                    #point = frame[527][635] #이건 재승이형이 맨 처음 부탁
                    B, G, R = self.Get_RGB(point_center)

                    self.center_b.append(B)
                    self.center_g.append(G)
                    self.center_r.append(R)

                    point_side = frame[520,396]
                    B, G, R = self.Get_RGB(point_side)

                    self.side_b.append(B)
                    self.side_g.append(G)
                    self.side_r.append(R)


                    self.x.append(self.i)
                    self.frames.append(frame)

                self.i += 1

            else:
                break
        self.Img_to_dataframe(self.frames)

    def Get_RGB(self, point):
        B = point[0]
        G = point[1]
        R = point[2]

        return (B,G,R)


    def Sub_plot(self, ax, x, y1, y2, Title):
        ax.plot(x, y1, label = 'Center')
        ax.plot(x, y2, label = 'Side')
        ax.set_xlabel("number of frame")
        ax.set_ylabel("Intensity")
        ax.legend()
        ax.set_title(Title)

    def Plot(self):

        fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1)
        fig.set_size_inches(10.5, 18.5)

        self.Sub_plot(ax1,self.x,self.center_b,self.side_b,'Blue')
        self.Sub_plot(ax2, self.x, self.center_g,self.side_g, 'Green')
        self.Sub_plot(ax3, self.x, self.center_r,self.side_r, 'Red')

        plt.show()





    def Img_to_dataframe(self, img_list):


        B_data = []
        G_data = []
        R_data = []


        for i in range(np.shape(img_list)[0]):

            frame = img_list[i]
            print('pixel 출력')

            B_frame = frame[:,:,0]
            print(np.shape(B_frame))
            B_data.append(B_frame.reshape(-1))
        print(np.shape(B_data))
        np.savetxt("test.csv", B_data, delimiter=",")







A = Anessa()