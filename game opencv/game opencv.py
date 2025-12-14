import cv2
import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
import time
import random

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
score = 0
x_enemy = random.randint(50, 600)
y_enemy = random.randint(50, 400)

def enemy():
    global score, x_enemy, y_enemy
    cv2.circle(image, (x_enemy, y_enemy), 25, (0, 200, 0), 5)


video = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageh, imagew, _ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 255)
        cv2.putText(image, "score", (480, 30), font, 1, color, 4, cv2.LINE_AA)
        cv2.putText(image, str(score), (590, 30), font, 1, color, 4, cv2.LINE_AA)
        enemy()

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))
                
                # Get index finger tip coordinates
                for point in mp_hands.HandLandmark:
                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP:
                        normalized_landmark = hand_landmarks.landmark[point]
                        pixel_coordinates = mp_drawing._normalized_to_pixel_coordinates(
                            normalized_landmark.x, normalized_landmark.y, imageh, imagew)
                      

                        
                        
                        if pixel_coordinates:
                            
                            cv2.circle(image, (pixel_coordinates[0], pixel_coordinates[1]), 25, (0, 0, 255), 5)

                            # Check if the finger is near the enemy circle
                            if abs(pixel_coordinates[0] - x_enemy) < 80 and abs(pixel_coordinates[1] - y_enemy) < 80:
                                print("Caught!")
                                
                                x_enemy = random.randint(50, 500)
                                y_enemy = random.randint(50, 400)
                                score += 1

        cv2.imshow('hand tracking', image)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
