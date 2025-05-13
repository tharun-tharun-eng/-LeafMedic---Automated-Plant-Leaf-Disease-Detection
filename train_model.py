# train_model.py

import os
import json
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import matplotlib.pyplot as plt

# — Paths & Setup —
DATA_DIR       = "data/PlantVillage"      # Folder containing subfolders per class
MODEL_DIR      = "model"
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH     = os.path.join(MODEL_DIR, "disease_model.keras")
CLASS_IDX_PATH = os.path.join(MODEL_DIR, "class_indices.json")

# — Hyperparameters —
IMG_SIZE   = 224
BATCH_SIZE = 32
EPOCHS     = 10

# — Data Generators with Augmentation & Validation Split —
datagen = ImageDataGenerator(
    preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

train_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)
val_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# — Save Class Indices for Later —
with open(CLASS_IDX_PATH, 'w') as f:
    json.dump(train_gen.class_indices, f)

# — Build Model: Transfer Learning with MobileNetV2 Base —
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False  # Freeze base

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(train_gen.num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# — Callbacks for Training —
callbacks = [
    EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1),
    ModelCheckpoint(MODEL_PATH, monitor='val_loss', save_best_only=True)
]

# — Train the Model —
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS,
    callbacks=callbacks
)

# — Save Final Model & Plot History —
model.save(MODEL_PATH)
print(f"Trained model saved to {MODEL_PATH}")

# Plot accuracy & loss curves
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.legend(); plt.title('Accuracy')

plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.legend(); plt.title('Loss')

plt.tight_layout()
plt.savefig(os.path.join(MODEL_DIR, 'training_history.png'))
print("Training history plot saved.")
