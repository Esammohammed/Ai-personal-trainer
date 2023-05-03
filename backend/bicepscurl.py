from datetime import datetime, timedelta

from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
import cv2
import mediapipe as mp
import numpy as np
import Pose_Estimation
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMainWindow, QLineEdit, QWidget, QPlainTextEdit, QTextEdit
def main (ui,cap):


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    stage = None
    oldhints = ''
    new_hints = ''
    new_hints+="Stand straight with a dumbbell in  hand,\nyour feet shoulder-width apart, and hands by your sides."
    def drawhints ():
        print (oldhints)
        ui.textbox.setText(oldhints);

    framenumber = 0
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

        while cap.isOpened():

            framenumber= framenumber+1
            # Extract landmarks
            try:
                results, image = Pose_Estimation.MakedetectionandExtract(pose, cap);
            except:
                break

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
                            tuple(np.multiply(elbow, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if angle > 160:
                    stage = "down"
                    if new_hints!='':
                        new_hints +='\n'
                    new_hints +="Great jop, Squeeze the biceps and lift the dumbbells.\nKeep the elbows close to your body"
                if angle < 40 and stage == 'down':
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

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

            if new_hints!= oldhints and new_hints != '':
                oldhints = new_hints
                drawhints()
            new_hints = ''

            winname = 'Mediapipe Feed'
            cv2.namedWindow(winname)
            cv2.moveWindow(winname, 600, 35)
            cv2.imshow(winname, image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        cv2.destroyAllWindows()

        duration = framenumber / fps
        Remainingtime = str(timedelta(seconds=duration)).split('.')[0]
        ui.Rmtime = Remainingtime
        ui.Repscount = counter
        ui.textbox.setText("Great job, generate report for more details");
        ui.getexersiceinformation()
        ui.Trainingname = 'bicepscurl'