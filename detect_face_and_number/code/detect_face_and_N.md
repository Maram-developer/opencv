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
