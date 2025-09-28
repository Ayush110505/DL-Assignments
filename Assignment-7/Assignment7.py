from ultralytics import YOLO

model = YOLO('yolov10n.pt')  # Load a pre-trained YOLOv10 model

results = model.predict(source='0', show=True, conf=0.25, save= True)  # Use webcam as source, display results, set confidence threshold