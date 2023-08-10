from ultralytics import YOLO

model = YOLO('yolov8n.pt') # pass any model type
model.train(data= "config.yaml", epochs=1, imgsz=640)