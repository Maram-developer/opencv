# Real-Time Face Detection using MediaPipe and OpenCV

This project implements a real-time face detection system using **MediaPipe** and **OpenCV**. 
It captures live video from a webcam, detects faces, and visualizes detection results with bounding boxes and keypoints.

## Pipeline
- Capture video from webcam
- Convert frames from BGR to RGB (required by MediaPipe)
- Process frames using MediaPipe Face Detection
- Draw detected faces with bounding boxes and landmarks
- Display the number of detected faces on the frame
- Show live video feed with detection overlays

## Features
- Real-time face detection
- Count the number of faces in the frame
- Visual feedback using bounding boxes and landmarks
- Works with a standard webcam

## Technologies Used
- Python
- OpenCV
- MediaPipe

## Input
- Live video stream from the default webcam

## Output
- Live video feed with detected faces outlined by bounding boxes
- Face landmarks drawn on each detected face
- Number of faces displayed on the top-left corner
