from datetime import datetime, timedelta

import cv2
import mediapipe as mp
import numpy as np
import Pose_Estimation
def main (ui,cap):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    # Curl counter variables
    counter = 0
    stage = 'down'
    oldhints = ''
    new_hints = ''
    new_hints += "Stand tall, a dumbbell in each hand\nRaise your arms simultaneously just a couple inches out to each side\nand pause."
    def drawhints():

        ui.textbox.setText(oldhints);
    ## Setup mediapipe instance

    framenumber = 0
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, ll = cap.read()
            if (ret==False):
                break
            framenumber = framenumber + 1
            try:
                results, image = Pose_Estimation.MakedetectionandExtract(pose, cap);
            except:
                break

            try:
                landmarks = results.pose_landmarks.landmark

                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_hip =  [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                #right
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]


                # Calculate angle
                angle1 = Pose_Estimation.calculate_angle(left_elbow, left_shoulder, right_hip)
                angle2= Pose_Estimation.calculate_angle(right_elbow,right_shoulder , right_hip)

                # Visualize angle
                cv2.putText(image, str(angle1),
                            tuple(np.multiply(right_shoulder, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle2),
                            tuple(np.multiply(left_shoulder, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )


                # Curl counter logic
                if angle1 > 85 and angle2 >85 and stage == 'down':
                    stage = "up"
                    new_hints += "Lower the weights slowly bringing your arms back to your sides.\nBreathe out as you lower the dumbbells"
                if (angle1 < 45 and  angle2<45 and stage == "up"):
                    counter += 1
                    print(counter)
                    stage = "down"
                    new_hints += "Raise your arms simultaneously just a couple inches out to each side\nand pause."
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
            if new_hints != oldhints and new_hints != '':
                oldhints = new_hints
                drawhints()
            new_hints = ''
            winname = 'Mediapipe Feed'
            cv2.namedWindow(winname)
            cv2.moveWindow(winname, 600, 40)
            cv2.imshow(winname, image)
            cv2.imshow('Mediapipe Feed', image)

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
        ui.Trainingname = 'lateral raises'