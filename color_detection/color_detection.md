# Real-Time Color Detection using OpenCV

This project demonstrates a simple real-time color detection system using OpenCV. 
The system captures video from a webcam, reads the color of the center pixel, 
and labels it with a color name on the video frame.

## Features
- Capture live video from webcam
- Detect the color of the center pixel in real-time
- Display the color name on the video frame
- Visual feedback with a circle at the center

## How It Works
1. Capture each frame from the webcam.
2. Convert the frame from BGR to HSV color space.
3. Get the HSV value of the center pixel.
4. Determine the color based on HSV thresholds:
   - Red, Orange, Yellow, Green, Blue, Violet, Black, White
5. Draw a circle at the center and display the detected color.
6. Press `q` to exit the application.

## Technologies Used
- Python
- OpenCV

## Input
- Webcam feed

## Output
- Live video with the detected color name displayed
