# Face Detection using MediaPipe

This project implements a real-time face detection system using MediaPipe and OpenCV.
It detects faces from the webcam, draws bounding boxes, and displays the total number of detected faces.

## Pipeline
- Capture video from webcam
- Convert frames to RGB
- Use MediaPipe FaceDetection model
- Draw bounding boxes on detected faces
- Display the number of faces on the frame

## Features
- Real-time face detection
- Bounding box visualization
- Face count display

## Technologies Used
- Python
- OpenCV
- MediaPipe

## Input
- Webcam video stream

## Output
- Live video feed with detected faces outlined by bounding boxes
- Face landmarks drawn on each detected face
- Number of faces displayed on the top-left corner 
