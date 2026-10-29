

import json
from pathlib import Path
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Project folders
BASE_DIR = Path(__file__).resolve().parent

TRAIN_DIR = BASE_DIR / "processed_data" / "train"
VAL_DIR = BASE_DIR / "processed_data" / "validation"
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Image settings
IMG_SIZE = (128, 128)
BATCH_SIZE = 16
EPOCHS = 20

# Load training data
train_data = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# Load validation data
val_data = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# Get class names
class_names = train_data.class_names

with open(MODEL_DIR / "class_names.json", "w") as file:
    json.dump(class_names, file)

print("Classes:", class_names)

# Data augmentation
data_augmentation = models.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

# Improve data loading speed
AUTOTUNE = tf.data.AUTOTUNE

train_data = train_data.prefetch(buffer_size=AUTOTUNE)
val_data = val_data.prefetch(buffer_size=AUTOTUNE)

# Build CNN model
model = models.Sequential([
    layers.Input(shape=(128, 128, 3)),

    # Apply augmentation only during training
    data_augmentation,

    # Normalize pixel values
    layers.Rescaling(1.0 / 255),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),

    layers.Dense(len(class_names), activation="softmax")
])

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Save the best model
checkpoint = ModelCheckpoint(
    MODEL_DIR / "potato_cnn.keras",
    monitor="val_loss",
    save_best_only=True,
    verbose=1
)

# Stop training when validation loss stops improving
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=4,
    restore_best_weights=True
)

# Train model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS,
    callbacks=[checkpoint, early_stopping]
)

# Save final model
model.save(MODEL_DIR / "potato_cnn_final.keras")

print("\nCNN training completed.")
print("Best model:", MODEL_DIR / "potato_cnn.keras")
print("Final model:", MODEL_DIR / "potato_cnn_final.keras")
