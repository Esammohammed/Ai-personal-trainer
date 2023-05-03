import sys
from datetime import time
from threading import Thread, Lock

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import time as t
from datetime import datetime
import cv2


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(972, 667)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 630, 451, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 630, 451, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(24, 19, 931, 591))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Start Stream"))
        self.pushButton_2.setText(_translate("Dialog", "Record"))
        self.label.setText(_translate("Dialog", "TextLabel"))
class WebcamVideoStream :
    def __init__(self, src, width = 640, height = 480) :
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.stream.set(cv2.CAP_PROP_BUFFERSIZE, 5)
        self.FPS = 1/30
        self.FPS_MS = int(self.FPS * 1000)
        (self.grabbed, self.frame) = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self) :
        if self.started :
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        return self

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            t.sleep(self.FPS)
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        if self.thread.is_alive():
            self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()



class MainWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_cam)



    def start_cam(self):
        self.capture = WebcamVideoStream(src = 0).start()
        self.timer=QTimer(self)
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(0)

    def update_frame(self):
        self.image=self.capture.read()
        qformat = QImage.Format_Indexed8
        if len(self.image.shape) == 3:
            if self.image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        outImage = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
        outImage = outImage.rgbSwapped()

        self.label.setPixmap(QPixmap.fromImage(outImage))
        self.label.setScaledContents(True)
        return outImage



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainW = MainWindow()
    mainW.show()
    sys.exit(app.exec_())