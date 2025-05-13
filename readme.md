# 🌿 LeafMedic - Automated Plant Leaf Disease Detection

LeafMedic is a Streamlit web application that allows users to detect plant leaf diseases from uploaded images using deep learning. It enhances input images, runs predictions with a trained CNN model, and generates a detailed disease diagnosis report with visual charts.

> 🎓 Academic Project: "Automated Plant Leaf Disease Detection through Image Preprocessing and Deep Learning"  
> 🏫 Subject: Image Processing using Python  
> 🧠 Developed with TensorFlow, OpenCV, Streamlit

---

## 📸 App Preview

Here is a quick demo of the application in action:

![LeafMedic App Demo](assets/demo.gif)

---

## 🚀 Features

- ✅ Upload leaf images (JPG, PNG)  
- 🧪 Image enhancement using OpenCV (grayscale, histogram equalization, blur, sharpening)  
- 🌱 Deep learning model (MobileNetV2 + custom head) for classification  
- 📊 Top-5 prediction chart with Plotly  
- 📄 AI-generated textual report based on prediction  
- 💾 Report export as downloadable .txt  
- 🖼️ Spot detection overlay for visualizing infected regions  

---

## 🛠️ Tech Stack

- Interface: Streamlit  
- Image Handling: OpenCV, PIL  
- Model: TensorFlow, Keras (MobileNetV2)  
- Charts: Plotly  
- Report Gen: Python f-strings  
- Deployment: Localhost / Streamlit Cloud  

---

## 📁 Project Structure
```bash
plant_leaf_disease_app/
│
├── model/
│   ├── disease_model.keras
│   └── class_indices.json
│
├── utils/
│   ├── preprocess.py      # Enhance images
│   ├── predict.py         # Load model & predict
│   └── report.py          # Generate report
│
├── app.py                 # Streamlit main app
├── train_model.py         # Model training script
├── requirements.txt
└── README.md
```
---

## 📦 Installation & Setup

1. Ensure Python 3.10+ is installed.
2. Create a virtual environment:

   ```bash
   python -m venv tf-env
   # Windows
   .\tf-env\Scripts\activate
   # macOS/Linux
   source tf-env/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501/](http://localhost:8501/)

---

## 🧪 How It Works

1. Upload a leaf image.
2. Preprocess with OpenCV: resize → grayscale → histogram equalization → Gaussian blur → unsharp masking.
3. Spot Detection: Otsu thresholding + contour bounding boxes.
4. Predict: CNN (MobileNetV2 backbone) outputs softmax probabilities.
5. Visualize: Show top-5 chart and confidence metric.
6. Report: Generate downloadable text report with description & treatment.

---

## 🧠 Concepts & Syllabus Mapping

| Topic                      | Implementation                              |
| -------------------------- | ------------------------------------------- |
| Grayscale & Histogram Eq.  | utils/preprocess.py (equalizeHist)          |
| Noise Removal & Sharpening | utils/preprocess.py (GaussianBlur, unsharp) |
| Thresholding & Contours    | app.py spot detection overlay               |
| Transfer Learning (CNN)    | train\_model.py (MobileNetV2 + head)        |
| Data Augmentation          | train\_model.py (ImageDataGenerator)        |
| Softmax & Metrics          | train\_model.py compile + fit               |
| Web UI & Charts            | app.py (Streamlit + Plotly)                 |
| Report Generation          | utils/report.py (f-strings)                 |

---

## 📄 requirements.txt

```text
streamlit>=1.40.2
tensorflow>=2.15.0
opencv-python>=4.9.0
pillow>=10.2.0
numpy>=1.26.4
matplotlib>=3.8.3
plotly>=5.22.0
scikit-learn>=1.4.2
```

---

## 📤 Deployment

* Streamlit Cloud: deploy with requirements.txt
* Docker (optional): add a Dockerfile
* Local: streamlit run app.py

---

## ✍️ Authors

* Srinidhi N S

---

## 📜 License

MIT License — for academic and educational use.

# -LeafMedic---Automated-Plant-Leaf-Disease-Detection
