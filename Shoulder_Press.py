from datetime import timedelta


def main (ui,cap):
    import cv2
    import mediapipe as mp
    import numpy as np

    import Pose_Estimation

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    counter = 0
    stage = None
    oldhints = ''
    new_hints = ''
    new_hints += "Stand with feet shoulder-width apart and hold the dumbbells at shoulder height with your elbows at a 90-degree angle."

    def drawhints():
        print(oldhints)
        ui.textbox.setText(oldhints);

    framenumber = 0;
    ##setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            framenumber=framenumber+1
            results,image = Pose_Estimation.MakedetectionandExtract(pose,cap);



            try:
                landmarks = results.pose_landmarks.landmark

                # get left coordinates
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                # get right coordinates
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                             landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                # calculate angles
                angle1 = Pose_Estimation.calculate_angle(right_shoulder, right_elbow, right_wrist)
                angle2 = Pose_Estimation.calculate_angle(left_shoulder, left_elbow, left_wrist)

                # visualize angle
                cv2.putText(image, str(angle1), tuple(np.multiply(right_elbow, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(angle2), tuple(np.multiply(left_elbow, [1280, 720]).astype(int)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                # CURL COUNTER LOGIC
                if angle1 >= 160 and angle2 >= 160:
                    stage = 'up'
                    new_hints+='Slowly return to the start position.'
                if angle1 >= 80 and angle1 <= 95  and angle2 >= 80 and angle2 <= 95 and stage == 'up':
                    stage = 'down'
                    counter += 1
                    new_hints += 'Slowly lift the dumbbells above your head without fully straightening your arms.\nPause at the top.'
            except:
                pass

            # render curl counter and setting up a status box
            cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

            # rep data
            cv2.putText(image, 'REPS', (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

            # stage data
            cv2.putText(image, 'STAGE', (65, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (60, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

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
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        cv2.destroyAllWindows()
        duration = framenumber / fps
        Remainingtime = str(timedelta(seconds=duration)).split('.')[0]
        ui.Rmtime = Remainingtime
        ui.Repscount = counter
        ui.textbox.setText("Great job, generate report for more details");
        ui.Trainingname = 'shoulder press'