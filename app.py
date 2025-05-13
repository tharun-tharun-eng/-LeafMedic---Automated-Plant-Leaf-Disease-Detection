# app.py

import os
import streamlit as st
from PIL import Image
import numpy as np
import cv2
import pandas as pd
import plotly.express as px

from utils.preprocess import preprocess_image
from utils.predict import predict_leaf_disease, labels as CLASS_LABELS
from utils.report import generate_disease_report

# --- Page Configuration & Styling ---
st.set_page_config(
    page_title="LeafMedic 🌿",
    page_icon="🍃",
    layout="wide"
)

st.markdown("""
    <style>
    footer {visibility: hidden;}
    .reportview-container {background-color: #f7fdfb; color: #333;}
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.6em 1.2em;
    }
    .stButton>button:hover {background-color: #256428;}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2909/2909763.png", width=80)
    st.title("LeafMedic 🍃")
    st.markdown("Automated Plant Leaf Disease Diagnosis")


# --- Main Interface ---
st.title("🌱 Plant Leaf Analyzer")

uploaded_file = st.file_uploader("📂 Upload a leaf image (JPG/PNG)", type=["jpg", "jpeg", "png"])
if not uploaded_file:
    st.info("Upload a leaf image to begin.")
    st.stop()

# 1. Original Image
orig = Image.open(uploaded_file)
st.markdown("### 🖼 Original Image")
st.image(orig, use_container_width=True)

# 2. Enhanced Image
enhanced = preprocess_image(orig)
st.markdown("### 🧪 Enhanced Image")
st.image(enhanced, use_container_width=True)

# 3. Spot Detection Overlay
st.markdown("### 🔍 Spot Detection Overlay")
gray = cv2.cvtColor(enhanced, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
overlay = enhanced.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (255, 0, 0), 2)
st.image(overlay, use_container_width=True)

# 4. Prediction & Report
st.markdown("## 🧠 Prediction & Report")
label, confidence, all_probs = predict_leaf_disease(orig)
read_label = label.replace("___", " – ").replace("_", " ")
report_text = generate_disease_report(label, confidence)

# Display prediction and report one above the other
st.metric("🔮 Prediction", read_label, f"{confidence*100:.1f}%")
st.text_area("📄 Diagnosis Report", report_text, height=250)
st.download_button("⬇️ Download Report", report_text, "disease_report.txt", "text/plain")

# 5. Confidence Explorer (Plotly Chart)
st.markdown("## 📊 Confidence Explorer")
top_n = st.slider("Select number of top classes to display:", min_value=3, max_value=len(CLASS_LABELS), value=5)
indices = np.argsort(all_probs)[::-1][:top_n]
top_labels = [CLASS_LABELS[i].replace("___", " – ").replace("_", " ") for i in indices]
top_scores = [float(all_probs[i] * 100) for i in indices]

df = pd.DataFrame({
    "Class": top_labels,
    "Confidence (%)": top_scores
})

fig = px.bar(
    df,
    x="Confidence (%)",
    y="Class",
    orientation="h",
    color="Confidence (%)",
    color_continuous_scale="greens",
    text="Confidence (%)",
    height=400
)
fig.update_layout(
    yaxis=dict(autorange="reversed"),
    xaxis=dict(range=[0, 100]),
    margin=dict(l=10, r=10, t=30, b=30),
    showlegend=False
)
fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')

st.plotly_chart(fig, use_container_width=True)

# 6. Footer
st.markdown("---")
st.caption("© 2025 LeafMedic • Dept. of AI & DS • MSRIT")
# --- End of app.py ---
# Note: Ensure all utility functions and classes are defined in their respective files.
# This code is a Streamlit application for diagnosing plant leaf diseases using a pre-trained deep learning model.  