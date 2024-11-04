import mediapipe as mp
import cv2
import os
import uuid
import numpy as np

mp_drawing = mp.solutions.drawing_utils #type:ignore
mp_hands = mp.solutions.hands #type:ignore

print("success")

cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Mirror the frame horizontally
        frame = cv2.flip(frame, 1)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=4, circle_radius=2),
                                          )
        
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break 

cap.release()
cv2.destroyAllWindows()
