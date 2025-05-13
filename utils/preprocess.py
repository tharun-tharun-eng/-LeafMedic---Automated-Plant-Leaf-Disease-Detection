# utils/preprocess.py

import cv2
import numpy as np
from PIL import Image

def preprocess_image(pil_img: Image.Image, target_size: tuple = (224, 224)) -> np.ndarray:
    """
    Applies classical image preprocessing to a PIL image:
      1. Resize to target_size
      2. Convert to BGR (OpenCV)
      3. Convert to grayscale and equalize histogram
      4. Apply Gaussian blur and unsharp masking
      5. Convert back to RGB (3-channel) for model input and display
    
    Args:
      pil_img:    PIL Image input (RGB)
      target_size: (width, height) to resize
    
    Returns:
      3-channel RGB numpy array after preprocessing
    """
    # 1. Resize & ensure RGB
    img_rgb = pil_img.convert("RGB")
    img_rgb = img_rgb.resize(target_size)
    
    # 2. Convert RGB → BGR for OpenCV
    img = np.array(img_rgb)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # 3. Grayscale + histogram equalization
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eq   = cv2.equalizeHist(gray)
    
    # 4a. Gaussian blur
    blur = cv2.GaussianBlur(eq, (5, 5), 0)
    # 4b. Unsharp masking (sharpen)
    sharp = cv2.addWeighted(eq, 1.5, blur, -0.5, 0)
    
    # 5. Convert single-channel sharpened back to 3-channel RGB
    sharp_rgb = cv2.cvtColor(sharp, cv2.COLOR_GRAY2RGB)
    
    return sharp_rgb
