import torch
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')  # pass any model type
    torch.cuda.set_device(0)
    model.train(data="config.yaml", epochs=10, imgsz=640, device=0)
