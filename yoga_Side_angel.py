import threading
import Pose_Estimation
import cv2
import mediapipe as mp
import numpy as np
import Timer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
def main (ui):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture('ysa.mp4')
    print(cap.isOpened())
    Firsttime=True
    flag = True

    oldhints = ''
    new_hints = ''
    new_hints += "Exhale and step your left foot behind towards the back of the mat with front foot staying at the top."
    def drawhints():

        print(oldhints)
        ui.textbox.setText(oldhints);

    #cap = cv2.VideoCapture(0)

    # Curl counter variables
    counter = 0
    stage = None

    with mp_pose.Pose(min_detection_confidence=.5, min_tracking_confidence=.5) as pose:
        while cap.isOpened():
            a1=0
            a2=0
            a3=0
            results,image = Pose_Estimation.MakedetectionandExtract(pose,cap)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                # left leg

                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]



                # right
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                # right leg

                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                # Calculate angle
                angle1 = Pose_Estimation.calculate_angle(left_elbow, left_shoulder, left_hip)
                angle2 = Pose_Estimation.calculate_angle(right_elbow, right_shoulder, right_hip)
                angle3 = Pose_Estimation.calculate_angle(left_ankle, left_knee, left_hip)
                angle4 = Pose_Estimation.calculate_angle(right_ankle, right_knee, right_hip)
                angle5 = Pose_Estimation.calculate_angle(left_knee, left_shoulder, left_hip)
                angle6 = Pose_Estimation.calculate_angle(right_knee, right_shoulder, right_hip)

                # Visualize arms
                cv2.putText(image, str(angle1),
                            #for recorded live  dimentions are [640, 480]
                            tuple(np.multiply(left_shoulder, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,(225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle2),
                            tuple(np.multiply(right_shoulder, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX,1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle3),
                            tuple(np.multiply(left_knee, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX,1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle4),
                            tuple(np.multiply(right_knee, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str( angle5),
                            tuple(np.multiply(left_hip, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA)
                cv2.putText(image, str(angle6),
                            tuple(np.multiply(right_hip, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX,1, (225, 230, 0), 2, cv2.LINE_AA)


                # Curl counter logic for arms

                if ((130 <= angle1 and angle1 <= 150) and ( 55 <= angle2  and angle2<= 75)):
                    a1 = 1
                else :
                    new_hints += 'Lift and extend your arms out horizontally from your sides, with palms down.\n' \
                                 'Angle your right heel toward the center of your mat\n'



                if 100 <= angle4 <= 125 and (170 <= angle3 <= 180 or 0 <= angle3 <= 10 ):
                    a2 = 1
                else :
                    new_hints += 'make your ankle closer to your body to make 90 \ndegree angle with your thigh\n' \
                                 'make your leg straight  to make 180 degree angle \nbetween your thigh and ankle\n'

                    # Visualize sides

                    # Curl counter logic for body sides

                if 60 <= angle6 <= 80 and  (0 <= angle5 <= 10 or 170 <= angle5 <= 180 ):

                    a3 = 1
                else:
                    new_hints+= "go with your left side to make 35 \ndegree angle with your  thigh\n" \
                                "make your right side straight  to\nq make 180 degree angle between your thigh and right side\n"


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
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )
            if new_hints != oldhints and new_hints != '':
                oldhints = new_hints
                drawhints()
            new_hints = ''
            if (((a1 == 1) and (a2 == 1)) and (a3 == 1)):
                new_hints = "keep your body at this pose"
                if Firsttime:
                    t1 = threading.Thread(target=Timer.lol)
                    t1.start()
                    Firsttime = False
                    flag =False
                    print("first")
                if flag:
                    print("start")
                    Timer.app.start()
                    flag = False

            elif ((flag == False) and (a1 != 1 or a2 != 1 or a3 != 1)):
                print("pause")
                flag = True
                Timer.app.pause()


            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        ui.report()