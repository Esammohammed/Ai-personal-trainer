from datetime import timedelta

import cv2
import mediapipe as mp
import numpy as np

import Pose_Estimation


def main(ui,cap):
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

    framenumber = 0;
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, ll = cap.read()
            if (ret == False):
                break
            framenumber = framenumber + 1
            try:
                results, image = Pose_Estimation.MakedetectionandExtract(pose, cap);
            except:
                break
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]



                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]


                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]

                # Calculate angle
                first_angle = Pose_Estimation.calculate_angle(left_shoulder, left_elbow, left_wrist)
                second_angle = Pose_Estimation.calculate_angle(right_shoulder, right_elbow, right_wrist)
                #body

                first_angle_body = Pose_Estimation.calculate_angle(left_shoulder, left_hip, left_knee)
                second_angle_body = Pose_Estimation.calculate_angle(right_shoulder, right_hip, right_knee)

                # Visualize angle
                cv2.putText(image, str(first_angle),
                            tuple(np.multiply(left_elbow, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(second_angle),
                            tuple(np.multiply(right_elbow, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                #body

                cv2.putText(image, str(first_angle_body),
                            tuple(np.multiply(left_hip, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(second_angle_body),
                            tuple(np.multiply(right_hip, [640, 360]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                # Curl counter logic
                if  170 >=first_angle >= 160 and 170 >= second_angle >= 160:
                    stage = "up"
                    new_hints+='Lower your body until your chest nearly touches the floor.\n' \
                               'Pause, then push yourself back up. Repeat.'

                if 70 >=first_angle >= 50 and 70 >= second_angle >= 50 and stage == 'up':
                    stage = "down"
                    if 180 >= first_angle_body >= 160 and 180 >= second_angle_body >= 160:
                        counter += 1
                        new_hints+="Get down on all fours, placing your hands slightly wider than your shoulders.\nStraighten your arms and legs."

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
            cv2.moveWindow(image, 40, 30)
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
        ui.Trainingname = 'push up'