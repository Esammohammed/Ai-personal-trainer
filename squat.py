from datetime import datetime

import cv2
import mediapipe as mp
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
import Pose_Estimation
def main (ui,cap):

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    stage = None

    oldhints = ''
    new_hints = ''
    new_hints += "Stand straight with feet hip-width apart."
    def drawhints():
        print(oldhints)
        ui.textbox.setText(oldhints);

    dt1 = datetime.now()
    framenumber=0;
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            framenumber=framenumber+1
            results,image = Pose_Estimation.MakedetectionandExtract(pose,cap);
            try:
                landmarks = results.pose_landmarks.landmark

                # get right coordinates
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                right_ankel = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                # get right coordinates
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                left_ankel = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # calculate angles
                angle1 = Pose_Estimation.calculate_angle(right_hip, right_knee, right_ankel)
                angle2 = Pose_Estimation.calculate_angle(left_hip, left_knee, left_ankel)

                # visualize angle
                cv2.putText(image, str(angle1), tuple(np.multiply(right_knee, [854,480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(angle2), tuple(np.multiply(left_knee, [854,480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                # CURL COUNTER LOGIC
                if angle1 > 160 and angle2 > 160:
                    stage = 'up'
                    new_hints += "Tighten your stomach muscles"
                    new_hints += "\nLower down, as if sitting in an invisible chair."
                if angle1 > 90 and angle1 < 110 and angle1 > 90 and angle1 < 110 and stage == 'up':
                    stage = 'down'
                    counter += 1
                    new_hints += 'Straighten your legs to lift back up.'
                    # print(counter)

                # print(landmarks)
            except:
                pass

            # render curl counter and setting up a status box
            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            # rep data
            cv2.putText(image, 'REPS', (15, 12), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 255, 255), 2, cv2.LINE_AA)

            # stage data
            cv2.putText(image, 'STAGE', (65, 12), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (60, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 255, 255), 2, cv2.LINE_AA)

            # rendering detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))
            if new_hints != oldhints and new_hints != '':
                oldhints = new_hints
                drawhints()
            new_hints = ''
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break;
        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        duration = framenumber / fps
        minutes = int(duration / 60)
        seconds = duration % 60
        print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        cap.release()
        cv2.destroyAllWindows()
        dt2 = datetime.now()


        Remainingtime = str(dt2 - dt1)
        timeh_m_sformat = Remainingtime.split('.')
        ui.Rmtime = timeh_m_sformat[0]
        print(timeh_m_sformat[0])
        ui.Repscount = counter
        ui.textbox.setText("Great job, generate report for more details");
        ui.Trainingname = 'squat'
