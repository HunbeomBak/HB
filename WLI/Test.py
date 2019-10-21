from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import cv2

#set cam
cam = cv2.VideoCapture('../data/20190917.avi')

## Create a GL View widget to display data
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.resize(600,400)
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=30)

## Add a grid to the view
g = gl.GLGridItem()
g.scale(2,2,1)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

## compute surface vertex data
cols = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
rows = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
x = np.linspace(0, 15, rows)
y = np.linspace(0, 15, cols)

## precompute height values for all frames
z = np.ones((rows,cols))

## create a surface plot, tell it to use the 'heightColor' shader
## since this does not require normal vectors to render (thus we 
## can set computeNormals=False to save time when the mesh updates)
p4 = gl.GLSurfacePlotItem(x=x, y = y, shader='heightColor', computeNormals=False, smooth=False)
p4.shader()['colorMap'] = np.array([0.2, 2, 0.5, 0.2, 1, 1, 0.2, 0, 2])
p4.translate(-5, -5, 0)
w.addItem(p4)

while 1:
    ret, img = cam.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = np.reshape(img, (np.shape(img)[0],np.shape(img)[1],1))

    #cv2.imshow("Cam Viewer", img)
    z = img/np.max(img) * 5

    p4.setData(z=z)
    pg.QtGui.QApplication.processEvents()
    if cv2.waitKey(1) == 27: # esc 누르면 종료
        win.close()
        break

cam.release()
cv2.destroyAllWindows()

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
