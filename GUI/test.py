import threading

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread

import Pose_Estimation
import cv2
import mediapipe as mp
import numpy as np

from pyqt5_plugins.examplebutton import QtWidgets

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 1280
        self.display_height = 720
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)

        # create a text label
        self.textLabel = QLabel('Hints')
        self.textBrowser = QLabel('label')

        font = QtGui.QFont()
        font.setPointSize(16)
        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textLabel.setFont(font)
        self.textLabel.setObjectName("label")

        # create a vertical box layout and add the two labels

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        vbox.addWidget(self.label)
        vbox.addWidget(self.textBrowser)

        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        self.setGeometry(100, 60, 950, 950)
        # create the video capture thread


        self.thread = VideoThread(self.textBrowser)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def showhints(self, zz):
        self.textBrowser.setText(zz)
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self,xx):
        self.__xx = xx
        super().__init__()

    def run(self):
        self.__xx.setText('asdas')
        try:
            pass
        except Exception as EX:
            print (EX)
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        # for recorded vidoe

        cap = cv2.VideoCapture('bi.mp4')
        #  cap = cv2.VideoCapture(0)
        print(cap.isOpened())
        # Curl counter variables
        counter = 0
        stage = None
        oldhints = ''
        new_hints = ''
        new_hints += "Stand straight with a dumbbell in  hand,\nyour feet shoulder-width apart, and hands by your sides."
        oldhints = new_hints

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

            while cap.isOpened():
                # Extract landmarks
                results, image = Pose_Estimation.MakedetectionandExtract(pose, cap);

                try:
                    landmarks = results.pose_landmarks.landmark

                    # Get coordinates
                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                    # Calculate angle
                    angle = Pose_Estimation.calculate_angle(shoulder, elbow, wrist)

                    # Visualize angle
                    cv2.putText(image, str(angle),
                                tuple(np.multiply(elbow, [640, 480]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                )

                    # Curl counter logic
                    if angle > 160:
                        stage = "down"
                        if new_hints != '':
                            new_hints += '\n'
                        new_hints += "Great jop, Squeeze the biceps and lift the dumbbells.\nKeep the elbows close to your body"
                    if angle < 35 and stage == 'down':
                        stage = "up"
                        if new_hints != '':
                            new_hints += '\n'
                        new_hints += "nice, slowly lower the arms to the starting position"
                        counter += 1
                        print(counter)

                except:
                    pass

                # Render curl counter
                # Setup status box
                cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

                # Rep data
                cv2.putText(image, 'REPS', (15, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter),
                            (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

                # Stage data
                cv2.putText(image, 'STAGE', (65, 12),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, stage,
                            (60, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                if new_hints != oldhints and new_hints != '':
                    oldhints = new_hints

                new_hints = ''

                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )


                self.change_pixmap_signal.emit(image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()





if __name__ == "__main__":

    app = QApplication(sys.argv)

    a= App()

    a.show()

    sys.exit(app.exec_())