from ultralytics import YOLO

# Load a model
model = YOLO("yolov5m.pt")  # load a pretrained model (recommended for training)

# Use the model
result = model.predict(source="0", show=True)  # train the model