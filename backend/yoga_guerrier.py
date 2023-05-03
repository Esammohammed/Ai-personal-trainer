from datetime import datetime


def main(ui,cap):
    import threading
    import Pose_Estimation
    import cv2
    import mediapipe as mp
    import numpy as np
    import Timer

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    Firsttime = True
    flag = False

    def calculate_angle(a, b, c):
        a = np.array(a)  # First
        b = np.array(b)  # Mid
        c = np.array(c)  # End
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle


    counter = 0
    stage = None
    oldhints = ''
    new_hints = ''
    new_hints += ""

    def drawhints():
        print(oldhints)
        ui.textbox.setText(oldhints);
    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            a1 = 0
            a2 = 0
            a3 = 0
            try:
                results, image = Pose_Estimation.MakedetectionandExtract(pose, cap);
            except:
                break
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
                angle1 = calculate_angle(left_elbow, left_shoulder, left_hip)
                angle2 = calculate_angle(right_elbow, right_shoulder, right_hip)
                angle3 = calculate_angle(left_ankle, left_knee, left_hip)
                angle4 = calculate_angle(right_ankle, right_knee, right_hip)
                angle5 = Pose_Estimation.calculate_angle(left_knee, left_shoulder, left_hip)
                angle6 = calculate_angle(right_knee, right_shoulder, right_hip)

                # Visualize arms
                cv2.putText(image, str(angle1),
                            # for recorded live  dimentions are [640, 480]
                            tuple(np.multiply(left_shoulder, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle2),
                            tuple(np.multiply(right_shoulder, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )

                # Curl counter logic for arms
                if angle1 > 115 or angle2 > 115:
                    new_hints += "your arm down to create 90 \ndegree with your body.\n"
                if angle1 < 85 or angle2 < 85:
                    new_hints += "raise your arm up to create 90 \ndegree with your body.\n"
                if 115 >= angle1 >= 85 and 115 >= angle2 >= 85:

                    a1 = 1
                    # counter += 1   put timer
                    # print(counter)

                # Visualize knees
                cv2.putText(image, str(angle3),
                            tuple(np.multiply(left_knee, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle4),
                            tuple(np.multiply(right_knee, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )

                # Curl counter logic for knees
                if angle3 > 115:
                    new_hints += "make your ankle closer to your \nbody to make 90 degree angle with your thigh.\n"
                if angle4 < 170:
                    new_hints += "make your leg straight to make\n180 degree angle between your thigh and ankle.\n"
                if angle3 < 90:
                    new_hints += "take step away with your left \nankle to make 90  degree angle with your thigh.\n"
                if 90 <= angle3 <= 115 and (170 <= angle4 <= 180 or 0 <= angle4 <= 10):
                    a2 = 1

                # Visualize sides
                cv2.putText(image, str(angle5),
                            tuple(np.multiply(left_hip, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )
                cv2.putText(image, str(angle6),
                            tuple(np.multiply(right_hip, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 230, 0), 2, cv2.LINE_AA
                            )

                # Curl counter logic for body sides
                if angle5 > 25:
                    new_hints += "go down with your thigh to make 90\ndegree angle with your body. \n"
                if angle6 < 10 or angle6 > 20:
                    new_hints += "make your back straight  to make 135\ndegree angle between your thigh and back.\n"
                if angle5 < 20:
                    new_hints += "go up with your thigh to make 90 \ndegree angle with your body.\n"
                if 25 >= angle5 >= 20 and 20 >= angle6 >= 10:
                    a3 = 1

                print(a2)
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
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                Timer.app.quit()
                break

        cap.release()
        cv2.destroyAllWindows()
        ui.textbox.setText("Great job, generate report for more details");
        time = str(Timer.app.hours) + ':' + str(Timer.app.minutes) + ':' + str(Timer.app.seconds)
        d = datetime.strptime(time, "%H:%M:%S")
        ui.Rmtime =d.time()
        ui.Trainingname = 'Yoga Guerrier'