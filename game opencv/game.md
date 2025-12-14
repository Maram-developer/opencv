# Hand Tracking Game using MediaPipe and OpenCV

This project implements an interactive game using **hand tracking** via **MediaPipe** and **OpenCV**. 
The player controls a virtual "finger pointer" to catch randomly appearing targets (enemy circles) on the screen, scoring points for each successful catch.

## Features
- Real-time hand tracking using webcam
- Index finger tip acts as a pointer to interact with targets
- Randomly appearing targets for dynamic gameplay
- Score counter displayed in real-time
- Simple, interactive, and fun application

## How It Works
1. Capture video from the webcam.
2. Use MediaPipe's Hands module to detect and track hand landmarks.
3. Map the index finger tip coordinates to screen pixels.
4. Draw targets (enemy circles) randomly on the screen.
5. Detect collisions between the index finger tip and the targets.
6. Update the score for each successful hit.
7. Press `q` to exit the game.

## Technologies Used
- Python
- OpenCV
- MediaPipe

## Input
- Live webcam feed: the game captures real-time video from your webcam to detect and track your hand movements.
- Player’s hand movements: the index finger tip is used to interact with the targets.

## Output
- Real-time video window showing:
  - Hand landmarks and connections for detected hands
  - Randomly appearing enemy circles
  - Score counter that updates when the player successfully touches a target
- Console logs (optional) showing "Caught!" each time a target is hit
