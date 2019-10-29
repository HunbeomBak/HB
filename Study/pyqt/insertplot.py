import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
import cv2
import numpy as np

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.imvplot()

    def initUI(self):
        self.guiplot = pg.PlotWidget()
        self.setWindowTitle('Xauron')
        self.setWindowIcon(QIcon('sauron.jpg'))
        self.setGeometry(300,300,600,400)
        self.show()
        layout = QGridLayout(self)
        layout.addWidget(self.guiplot, 0,0)

    def imvplot(self):
        data = cv2.imread('cat.jpg')
        data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
        data = np.array(data)
        self.imv = pg.ImageView(data)
        
        self.guiplot.addItem(self.imv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
