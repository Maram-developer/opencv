# Yellow Line Detection

This project detects yellow lines in a live video feed using OpenCV. It uses **HSV color space** for color segmentation and the **Hough Line Transform** for line detection.

## How it works
1. Capture live video from the webcam.
2. Apply Gaussian blur to reduce noise.
3. Convert the frame to HSV color space.
4. Create a mask for yellow color using predefined HSV ranges.
5. Detect edges using Canny edge detection.
6. Detect lines in the masked edges using Hough Line Transform.
7. Draw detected lines on the original frame.

## Input
- Live webcam feed
- Yellow lines in the scene

## Output
- Real-time video showing:
  - Original frame with detected yellow lines drawn in green
  - Mask showing only yellow regions
  - Edges detected by the Canny detector

## Potential Applications
- Lane detection in self-driving cars
- Robotics path following
- Industrial automation for line following robots
