import os
import io
import torch

from ultralytics import YOLO
from PIL import Image


def load_model() -> YOLO:
    """
    Load the model from the specified directory.
    """

    model = YOLO("/app/src/model/yolov9c.pt")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    return model


def predict(image_data: bytes, model: YOLO) -> dict:
    """
    Generate predictions for the incoming request using the model.
    """

    image_pil = Image.open(
        io.BytesIO(image_data)
    )  # Convert the image from bytes to PIL Image

    with torch.no_grad():
        inference_result = model.predict(image_pil)  # Get inference on image

    inference_result = get_bounding_boxes(inference_result)  # Get bounding boxes

    return inference_result


def get_bounding_boxes(inference_result: list) -> dict:
    """
    Extract bounding boxes from the inference result.
    """
    infer = {}

    for result in inference_result:
        if result.boxes:
            infer["bounding_boxes"] = result.boxes.numpy().data.tolist()

    return infer
