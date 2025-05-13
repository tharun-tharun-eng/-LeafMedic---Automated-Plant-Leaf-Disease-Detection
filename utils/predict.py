# utils/predict.py

import os
import json
import functools
from typing import Tuple

import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing import image as kimage

# Paths
MODEL_PATH = os.path.join("model", "disease_model.keras")
CLASS_IDX_PATH = os.path.join("model", "class_indices.json")

# Load and cache model
@functools.lru_cache(maxsize=1)
def load_model() -> tf.keras.Model:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
    try:
        return tf.keras.models.load_model(MODEL_PATH, compile=False)
    except Exception as e:
        print("❌ Failed to load model from:", MODEL_PATH)
        print("🔍 Detailed exception:", repr(e))
        raise RuntimeError("Model loading failed.")

model = load_model()

# Load class indices
if not os.path.exists(CLASS_IDX_PATH):
    raise FileNotFoundError(f"Class index file not found at: {CLASS_IDX_PATH}")

with open(CLASS_IDX_PATH, "r") as f:
    class_indices = json.load(f)

# Build a label list where labels[i] = class name for model output index i
labels = [None] * len(class_indices)
for class_name, idx in class_indices.items():
    if not isinstance(idx, int) or idx < 0 or idx >= len(labels):
        raise ValueError(f"Invalid class index for '{class_name}': {idx}")
    labels[idx] = class_name

if any(label is None for label in labels):
    raise ValueError("Class indices mapping is incomplete or contains gaps.")

def predict_leaf_disease(
    pil_img: Image.Image,
    target_size: Tuple[int, int] = (224, 224)
) -> Tuple[str, float, np.ndarray]:
    """
    Predicts the disease class of a plant leaf image.

    Args:
        pil_img: A PIL.Image.Image object (can be RGB or grayscale).
        target_size: Tuple (width, height) to resize the image for the model.

    Returns:
        predicted_label: The class name (folder key) with highest probability.
        confidence: Probability (0–1) of the predicted_label.
        all_probs: Numpy array of probabilities for all classes.
    """
    # Resize and convert to RGB
    img = pil_img.resize(target_size).convert("RGB")

    # Convert to array, normalize, and expand dims
    arr = kimage.img_to_array(img) / 255.0
    arr = np.expand_dims(arr, axis=0)

    # Predict
    preds = model.predict(arr)[0]
    top_idx = int(np.argmax(preds))

    return labels[top_idx], float(preds[top_idx]), preds
