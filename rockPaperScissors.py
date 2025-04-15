import cv2 as cv
import mediapipe as mp
import random
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

last_ai_update = time.time()
ai_move = random.choice(['Rock', 'Paper', 'Scissors'])

def hand_gesture(landmarks):
    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y
    ring_tip = landmarks[16].y
    pinky_tip = landmarks[20].y
    
    if index_tip > middle_tip and index_tip < ring_tip and index_tip < pinky_tip:
        return "Scissors"
    elif thumb_tip > index_tip and thumb_tip > middle_tip and thumb_tip > ring_tip and thumb_tip > pinky_tip:
        return "Paper"
    else:
        return "Rock"
    
def winner(player, ai):
    if player == ai:
        return "Draw"
    elif (player == "Rock" and ai == "Scissors") or (player == "Scissors" and ai == "Paper") or (player == "Paper" and ai == "Rock"):
        return "Player Wins!"
    else:
        return "AI Wins!"


while cap.isOpened():
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    player_move = "Unknown"
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)
            player_move = hand_gesture(handlms.landmark)


    if time.time() - last_ai_update > 2:
        ai_move = random.choice(["Rock", "Paper", "Scissors"])
        last_ai_update = time.time()

    result = winner(player_move, ai_move)

    cv.putText(img, f"Player: {player_move}", (10, 70), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv.putText(img, f"AI: {ai_move}", (10, 120), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.putText(img, result, (10, 170), cv.FONT_HERSHEY_SIMPLEX, 1, (100, 0, 255), 2)

    cv.imshow('Image', img)
    if cv.waitKey(1) == ord('q'):
        break