import cv2
import mediapipe as mp
import numpy as np

import Pose_Estimation
def main ():


    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    stage = None

    oldhints = ''
    new_hints = ''
    new_hints += "Stand straight with feet hip-width apart."
    def drawhints(image):
        print(oldhints)
        image = cv2.rectangle(image, (0, 770), (100 + 2000, 900), (0, 0, 0), -1)

        for i, line in enumerate(oldhints.split('\n')):
            cv2.putText(image, line, (550, 790+(i*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    '''
    # for live 
        image = cv2.rectangle(image, (0, 400), (100 + 2000, 900), (0, 0, 0), -1)
        for i, line in enumerate(oldhints.split('\n')):
            cv2.putText(image, line, (0, 420+(i*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    '''
    #for recorded vidoe
    #
    cap = cv2.VideoCapture('Squat.mp4')
    #cap = cv2.VideoCapture(0)

    ##setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
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
                cv2.putText(image, str(angle1), tuple(np.multiply(right_knee, [1280,720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(angle2), tuple(np.multiply(left_knee, [1280,720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                # CURL COUNTER LOGIC
                if angle1 > 160 and angle2 > 160:
                    stage = 'up'
                    new_hints += "Tighten your stomach muscles"
                    new_hints += "\nLower down, as if sitting in an invisible chair."
                if angle1 > 90 and angle1 < 110 and angle2 > 90 and angle2 < 110 and stage == 'up':
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
            drawhints(image)
            new_hints = ''
            cv2.imshow('Mediapipe Feed', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break;
        cap.release()
        cv2.destroyAllWindows()
main()