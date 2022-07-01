from datetime import datetime

import Pose_Estimation


def main(ui,cap):
    import cv2
    import mediapipe as mp
    import numpy as np
    import tkinter as tk
    import Timer
    import time
    import threading

    #cobra stretch
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    Firsttime=True
    flag = False
    oldhints = ''
    new_hints = ''
    def drawhints():

        print(oldhints)
        ui.textbox.setText(oldhints);


    counter = 0
    stage = None
    hand_right = 0
    body_right = 0
    leg_right = 0




    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            a1 = 0
            a2 = 0
            a3 = 0

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # hand
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                #body
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


                #leg
                left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                left_heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
                left_foot_index = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]

                right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                right_heel = [landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]
                right_foot_index = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]

                # Calculate angle (hand)
                first_angle_hand = Pose_Estimation.calculate_angle(left_shoulder, left_elbow, left_wrist)
                second_angle_hand = Pose_Estimation.calculate_angle(right_shoulder, right_elbow, right_wrist)

                # Calculate angle (body)

                first_angle_body = Pose_Estimation.calculate_angle(left_shoulder,left_hip, left_knee)
                second_angle_body = Pose_Estimation.calculate_angle(right_shoulder, right_hip, right_knee)

                # Calculate angle (leg)

                first_angle_leg = Pose_Estimation.calculate_angle(left_ankle, left_heel, left_foot_index)
                second_angle_leg = Pose_Estimation.calculate_angle(right_ankle, right_heel, right_foot_index)

                # Visualize angle
                #hand
                cv2.putText(image, str(first_angle_hand),
                            tuple(np.multiply(left_elbow, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(second_angle_hand),
                            tuple(np.multiply(right_elbow, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                #body
                cv2.putText(image, str(first_angle_body),
                           tuple(np.multiply(left_hip, [850, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                           )
                cv2.putText(image, str(second_angle_body),
                            tuple(np.multiply(right_hip, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )

                #leg
                cv2.putText(image, str(first_angle_leg),
                            tuple(np.multiply(left_heel, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(second_angle_leg),
                            tuple(np.multiply(right_heel, [850, 480]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                            )



                # Curl counter logic
                if  180 >= first_angle_hand >= 165 and 180 >= second_angle_hand >= 165:
                    a1 = 1
                else:
                    new_hints += 'Place your palms flat on the ground directly under your shoulders.\n' \
                                 'Bend your elbows straight back and hug them into your sides\n'


                if  140 >= first_angle_body >= 100 and 140 >= second_angle_body >= 100 :
                    a2 = 1
                else:
                    new_hints += 'Inhale to lift your chest off the floor. Roll your shoulders back and keep your low ribs on the floor.\n' \
                                 'Make sure your elbows continue hugging your sides.\n' \



                if  70 >= first_angle_leg >= 40 and 70 >= second_angle_leg >= 40 :
                    a3 = 1
                else:
                    new_hints += 'Make sure that your pelvis and legs are firmly rooted into the floor.\n' \
                                 'They act as the anchor that allows your upper body to rise\n' \


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
                        flag = False
                        print("first")
                    if flag:
                        print("start")
                        Timer.app.start()
                        flag = False

                elif ((flag == False) and (a1 != 1 or a2 != 1 or a3 != 1)):
                    print("pause")
                    flag = True
                    Timer.app.pause()


            except:
                pass





            # Render curl counter
            # Setup status box
            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            # Rep data
            cv2.putText(image, 'REPS', (15, 12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(stage),
                        (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Stage data
           # cv2.putText(image, 'STAGE', (65, 12),
                     #   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            #cv2.putText(image, stage,
                       # (60, 60),
                       # cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                      )

            cv2.imshow('Mediapipe Feed', image)
            cv2.moveWindow('Mediapipe Feed', 550, 30)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                Timer.app.quit()
                break

        cap.release()
        cv2.destroyAllWindows()
        ui.textbox.setText("Great job, generate report for more details");
        time = str(Timer.app.hours) + ':' + str(Timer.app.minutes) + ':' + str(Timer.app.seconds)
        d = datetime.strptime(time, "%H:%M:%S")
        ui.Trainingname = 'Yoga stretch'
        ui.Rmtime = d.time()

        t1.join()