import cv2
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolov8n.pt")

# Perform object detection on a video using the model
# Set classes=2, show the cars only
results = model.track(source="C:/Users/user/course4/argoverse.mp4", show=True, save=True, tracker="bytetrack.yaml", classes=2)
