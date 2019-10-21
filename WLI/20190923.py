import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time


from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl


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

        self.I = []
        self.Phase = []

        self.i = 1


    def Road_Video(self):
        #self.cap = cv2.VideoCapture('./data/20190917.avi')
        self.cap = cv2.VideoCapture('../data/20190917.avi')

        self.nf = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 프레임 수
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.num_pixel = self.width * self.height
        print(self.nf)

    def Run(self):
        self.Plot3D()

        while True:
            ret, frame = self.cap.read()
            if ret:


                print(self.i)
                center = (np.shape(frame)[0:2])
                point_center = frame[520][696] # 가운데
                #point = frame[527][635] #이건 재승이형이 맨 처음 부탁

                self.Get_RGB(point_center, list_B=self.center_b, list_G=self.center_g, list_R=self.center_r)

                point_side = frame[520,396]
                self.Get_RGB(point_side, list_B=self.side_b, list_G=self.side_g, list_R=self.side_r)

                self.x.append(self.i)
                #self.frames.append(frame)

                self.i += 1


                self.PhaseSolve(frame)

            else:
                break
        #self.Img_to_dataframe(self.frames)

    def Get_RGB(self, point, list_B, list_G, list_R):
        B = point[0]
        G = point[1]
        R = point[2]

        list_B.append(B)
        list_G.append(G)
        list_R.append(R)


    def Sub_plot(self, ax, x, y1, y2, Title):
        ax.plot(x, y1, label = 'Center')
        ax.plot(x, y2, label = 'Side')
        ax.set_xlabel("number of frame")
        ax.set_ylabel("Intensity")
        ax.legend()
        ax.set_title(Title)

    def PhaseSolve(self,img):

        self.I.append(img)

        n = len(self.I)



        if n ==5:

            분자 =  2*(self.I[3]-self.I[1]) 
            분모 = (2*self.I[2] - self.I[0] - self.I[4])
            result = np.arctan2(분자, 분모)

            self.p4.setData(z=result[:,:,0])
            pg.QtGui.QApplication.processEvents()

            self.Phase.append(result)

            del self.I[0]

        else:
            pass


    def Plot(self):

        fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3, ncols = 1)
        fig.set_size_inches(10.5, 18.5)

        self.Sub_plot(ax1,self.x,self.center_b,self.side_b,'Blue')
        self.Sub_plot(ax2, self.x, self.center_g,self.side_g, 'Green')
        self.Sub_plot(ax3, self.x, self.center_r,self.side_r, 'Red')

        plt.show()

    def Plot3D(self):
        QtGui.QApplication([])
        w = gl.GLViewWidget()
        w.show()
        w.resize(600, 400)
        w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        w.setCameraPosition(distance=30)

        g = gl.GLGridItem()
        g.scale(2, 2, 1)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)

        cols = self.width
        rows = self.height
        x = np.linspace(0, 15, rows)
        y = np.linspace(0, 15, cols)

        ## precompute height values for all frames
        z = np.ones((rows, cols))

        self.p4 = gl.GLSurfacePlotItem(x=x, y=y, shader='heightColor', computeNormals=False, smooth=False)
        self.p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
        self.p4.translate(-5, -5, 0)
        w.addItem(self.p4)



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
A.Road_Video()
A.Run()

