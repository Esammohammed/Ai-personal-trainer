import sys
from cmath import rect

import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from joblib._multiprocessing_helpers import mp
import mediapipe as mp
import numpy as np
from pyqt5_plugins.examplebuttonplugin import QtGui

import Pose_Estimation
import cv2


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Video'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setGeometry(100, 60, 970, 950)
        #create a label
        label = QLabel(self)



        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose


        #for recorded vidoe

       # cap = cv2.VideoCapture('bi.mp4')
        cap = cv2.VideoCapture(0)
        print(cap.isOpened())
        # Curl counter variables
        counter = 0
        stage = None
        oldhints = ''
        new_hints = ''
        new_hints+="Stand straight with a dumbbell in  hand,\nyour feet shoulder-width apart, and hands by your sides."
        oldhints = new_hints





        # for recorded vidoe
        # for recorded vidoe

        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

            while cap.isOpened():
                # Extract landmarks
                results,image = Pose_Estimation.MakedetectionandExtract(pose,cap);
                convertToQtFormat = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                                                 QtGui.QImage.Format_RGB888)
                convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
                image = QPixmap(convertToQtFormat)
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
                        if new_hints!='':
                            new_hints +='\n'
                        new_hints +="Great jop, Squeeze the biceps and lift the dumbbells.\nKeep the elbows close to your body"
                    if angle < 35 and stage == 'down':
                        stage = "up"
                        if new_hints!='':
                            new_hints +='\n'
                        new_hints +="nice, slowly lower the arms to the starting position"
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
                if new_hints!= oldhints and new_hints !='':
                    oldhints=new_hints

                new_hints = ''
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )


                QApplication.processEvents()
                label.setPixmap(image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                self.show()

            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())