# RockPaperScissors_ComputerVision
 
This project is a fun and interactive implementation of the classic Rock-Paper-Scissors game using Computer Vision and Python. Instead of clicking buttons or typing inputs, the user plays by showing hand gestures (rock, paper, or scissors) in front of their webcam. The computer detects the gesture using image processing techniques and plays against the user in real-time.

🔍 Features
Real-time hand gesture recognition using webcam

Gesture classification for Rock, Paper, and Scissors

Random move generation by the computer

Score tracking and winner declaration

Simple and intuitive interface using OpenCV

🛠️ Technologies Used
Python

OpenCV for image processing

Mediapipe (or your own hand detection logic)

NumPy

📷 How It Works
The webcam captures the live video feed.

Hand landmarks are detected using Mediapipe.

Based on the finger positions, the program classifies the hand gesture into Rock, Paper, or Scissors.

The computer randomly selects its move.

The result is displayed along with updated scores.