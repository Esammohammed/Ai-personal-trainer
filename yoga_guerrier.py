def main():
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

    # cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture('Warrior_Pose_2.mp4')
    # Curl counter variables
    counter = 0
    stage = None

    ## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            a1 = 0
            a2 = 0
            a3 = 0
            results, image = Pose_Estimation.MakedetectionandExtract(pose, cap)

            ret, frame = cap.read()

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
                    stage = "your arm down to create 90 degree with your body"
                if angle1 < 85 or angle2 < 85:
                    stage = "raise your arm up to create 90 degree with your body"
                if 115 >= angle1 >= 85 and 115 >= angle2 >= 85:
                    stage = "keep you arms at this pose"
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
                    stage = "make your ankle closer to your body to make 90 degree angle with your thigh"
                if angle4 < 170:
                    stage = "make your leg straight  to make 180 degree angle between your thigh and ankle"
                if angle3 < 90:
                    stage = "take step away with your left ankle to make 90 degree angle with your thigh"
                if 90 <= angle3 <= 115 and (170 <= angle4 <= 180 or 0 <= angle4 <= 10):
                    stage = "keep you legs at this pose"
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
                    stage = "go down with your thigh to make 90 degree angle with your body"
                if angle6 < 10 or angle6 > 20:
                    stage = "make your back straight  to make 135 degree angle between your thigh and back"
                if angle5 < 20:
                    stage = "go up with your thigh to make 90 degree angle with your body"
                if 25 >= angle5 >= 20 and 20 >= angle6 >= 10:
                    stage = "keep you body at this pose"
                    a3 = 1

                print(a2)
                if a1 == 1 and a2 == 1 and a3 == 1:
                    stage = "timer starts"
                    if Firsttime:
                        t1 = threading.Thread(target=Timer.lol)
                        t1.start()
                        Firsttime = False

                    if flag:
                        Timer.app.start()
                        flag = True
                if a1 != 1 or a2 != 1 or a3 != 1:
                    Timer.app.pause()
                    flag = True

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

            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


main()
