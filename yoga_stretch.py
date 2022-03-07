import cv2
import mediapipe as mp
import numpy as np
import tkinter as tk
import Timer
import Pose_Estimation
import threading


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
Firsttime=True
flag = False
counter = 0

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle





cap = cv2.VideoCapture(0)

# Curl counter variables
counter = 0
stage = None
hand_right = 0
body_right =0
leg_right = 0




## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        results,image = Pose_Estimation.MakedetectionandExtract(pose,cap);

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
                        tuple(np.multiply(left_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(second_angle_hand),
                        tuple(np.multiply(right_elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )

            #body
            cv2.putText(image, str(first_angle_body),
                       tuple(np.multiply(left_hip, [640, 480]).astype(int)),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                       )
            cv2.putText(image, str(second_angle_body),
                        tuple(np.multiply(right_hip, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )

            #leg
            cv2.putText(image, str(first_angle_leg),
                        tuple(np.multiply(left_heel, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(second_angle_leg),
                        tuple(np.multiply(right_heel, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )



            # Curl counter logic
            if first_angle_hand > 150 and second_angle_hand > 150:
                stage = "correct hand"
                hand_right = 1
            else:
                hand_right = 0
            if first_angle_body > 130 and second_angle_body > 130 and stage == 'correct hand':
                stage = "correct body"
                body_right = 1
            else:
                body_right = 0
            if first_angle_leg > 50 and second_angle_leg > 50 and stage == 'correct body':
                stage = "correct leg"
                leg_right = 1
            else:
                leg_right = 0


        except:
            pass

        if hand_right == 1 and body_right == 1 and leg_right == 1:
            stage = "timer starts"
            if Firsttime:
                t1 = threading.Thread(target=Timer.lol)
                t1.start()
                Firsttime = False
                if flag :
                  Timer.app.start()
                  flag = True
            if hand_right != 1 or body_right != 1 or leg_right != 1:
                Timer.app.pause()
                flag = True






        # Render curl counter
        # Setup status box
        cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

        # Rep data
        cv2.putText(image, 'REPS', (15, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(),
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

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()