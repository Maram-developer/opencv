# Object Detection using OpenCV (Inference)

This project performs real-time object detection using OpenCV and a pre-trained SSD MobileNet v3 model.

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)

## Model & Data Files

The project requires the following files:

1. **Model config:** `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` (included in repo)
### Model Weights
Download the model weights here: [frozen_inference_graph.pb](https://www.kaggle.com/code/chienhsianghung/object-detection-using-opencv-inference/notebook)
Place the file inside the `models/` folder.


### Class Names

`coco.names` file included in `data/` folder.

## Usage

```bash
python scripts/detect_objects.py