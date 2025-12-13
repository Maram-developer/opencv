<<<<<<< HEAD
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
=======
# Eye Movement Detection using OpenCV

This project implements a real-time eye movement detection system using computer vision techniques. 
It processes a pre-recorded video to detect eye regions and visualize their movement.

## Project Overview
The system analyzes video frames to localize the eye region using contour detection and provides visual feedback in real time. 
It demonstrates how OpenCV can be applied to practical problems such as driver drowsiness detection.

## Pipeline
1. Convert video frames to grayscale.
2. Apply Gaussian blur to reduce noise.
3. Apply binary thresholding to isolate the eye region.
4. Detect contours and sort them by area.
5. Visualize detected contours with bounding boxes and center lines.

## Features
- Eye region localization using contours
- Real-time visualization
- Output video saving for later analysis
- Simple and easy-to-extend pipeline for research or prototyping

## Input
- Pre-recorded video containing eye movement (`input_video.mp4`)

## Output
- Processed video with detected eye contours (`output_video.mp4`)

## Technologies Used
- Python 3.x
- OpenCV

## Potential Applications
- Driver drowsiness detection systems
- Eye-tracking studies
- Human-computer interaction research
>>>>>>> 1993567e7e718ef029251084deb9a56a2eeb835a
