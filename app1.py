
"""
Company: Crevavi Technologies
Project: Potato Disease Detection using CNN
Interface: Streamlit
"""

from pathlib import Path
import json
from disease_recommendations import get_recommendation
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = MODEL_DIR / "potato_cnn_final.keras"
CLASS_PATH = MODEL_DIR / "class_names.json"


@st.cache_resource
def load_model():
    if not MODEL_PATH.is_file():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    return tf.keras.models.load_model(str(MODEL_PATH))


@st.cache_data
def load_classes():
    with open(CLASS_PATH, "r") as file:
        return json.load(file)


try:
    model = load_model()
    class_names = load_classes()
    st.success(f"Model loaded successfully: {MODEL_PATH.name}")

except Exception as error:
    st.error(f"Unable to load model: {error}")
    st.stop()


# Page settings
st.set_page_config(
    page_title="Potato Disease Detection",
    page_icon="🥔",
    layout="wide"
)


# Load trained model
@st.cache_resource
def load_model(model_path):
    return tf.keras.models.load_model(model_path)


# Load class names
@st.cache_data
def load_classes(class_path):
    with open(class_path, "r") as file:
        return json.load(file)


# Application title
st.title("🥔 Potato Disease Detection System")

st.write(
    "Upload a potato image to predict its condition "
    "and view treatment, fertilizer, and prevention guidance."
)

st.divider()


# Check required files
if not MODEL_PATH.exists():
    st.error(
        f"Trained model not found.\n\n"
        f"Expected folder: {MODEL_DIR}\n\n"
        "Run python train_model.py to train the model."
    )
    st.stop()

if not CLASS_PATH.exists():
    st.error(
        f"Class names file not found: {CLASS_PATH}\n"
        "Run python train_model.py first."
    )
    st.stop()


# Load model and classes
try:
    model = load_model(str(MODEL_PATH))
    class_names = load_classes(str(CLASS_PATH))
except Exception as error:
    st.error(f"Unable to load the model: {error}")
    st.stop()


st.caption(f"Loaded model: {MODEL_PATH.name}")

st.subheader("Upload Potato Image")

uploaded_file = st.file_uploader(
    "Choose a potato image",
    type=["jpg", "jpeg", "png", "bmp", "webp"]
)


if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")

        left, right = st.columns(2)

        with left:
            st.image(
                image,
                caption="Uploaded Potato Image",
                width="stretch"
            )

        with right:
            if st.button("Predict Disease", type="primary"):

                # Prepare image
                resized_image = image.resize((128, 128))

                image_array = np.asarray(
                    resized_image,
                    dtype=np.float32
                )

                image_array = np.expand_dims(
                    image_array,
                    axis=0
                )

                # Predict class
                probabilities = model.predict(
                    image_array,
                    verbose=0
                )[0]

                predicted_index = int(np.argmax(probabilities))
                predicted_class = class_names[predicted_index]

                confidence = float(
                    probabilities[predicted_index] * 100
                )

                # Display prediction
                st.subheader("Prediction Result")
                st.success(predicted_class.replace("_", " "))

                st.metric(
                    "Model Confidence",
                    f"{confidence:.2f}%"
                )

                # Display probabilities
                st.subheader("Class Probabilities")

                for index, class_name in enumerate(class_names):
                    percentage = float(probabilities[index] * 100)

                    st.write(
                        f"{class_name.replace('_', ' ')}: "
                        f"{percentage:.2f}%"
                    )

                    st.progress(
                        min(max(percentage / 100, 0.0), 1.0)
                    )

                # Treatment and fertilizer recommendations
                advice = get_recommendation(predicted_class)

                st.divider()
                st.header("🌱 Treatment and Fertilizer Guidance")

                st.subheader("Recommended Management")

                for item in advice["treatment"]:
                    st.markdown(f"- {item}")

                st.subheader("Fertilizer Guidance")
                st.info(advice["fertilizer"])

                st.subheader("Prevention")

                st.write(advice["prevention"])

                # Warnings
                if confidence < 60:
                    st.warning(
                        "The model confidence is low. "
                        "Verify the condition before taking action."
                    )

            

    except Exception as error:
        st.error(f"Unable to process image: {error}")


st.divider()


