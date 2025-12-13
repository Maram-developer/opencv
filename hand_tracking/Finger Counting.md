# Finger Counting with MediaPipe

This project implements a real-time finger counting system using a webcam. It leverages **MediaPipe Hands** for hand landmark detection and **OpenCV** for visualization.

## How it works
1. Capture live video from the webcam.
2. Detect hand landmarks using MediaPipe.
3. Determine which fingers are up by comparing landmark positions.
4. Display the total number of raised fingers on the screen in real-time.

## Input
- Live webcam feed
- Movements of the user's hand

## Output
- Real-time video window showing:
  - Hand landmarks and connections
  - Count of fingers currently raised
- Number displayed on the top-left of the video frame

## Potential Applications
- Gesture-based control systems
- Learning tools for kids to understand counting
- Interactive games and VR/AR applications
