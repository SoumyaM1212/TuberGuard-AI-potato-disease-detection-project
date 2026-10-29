
from pathlib import Path
import json
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
TEST_DIR = BASE_DIR / "processed_data" / "test"
REPORT_DIR = BASE_DIR / "reports"


def test_model():

    model_path = MODEL_DIR / "potato_cnn.keras"
    class_path = MODEL_DIR / "class_names.json"

    if not model_path.exists() or not class_path.exists():
        raise FileNotFoundError(
            "Model files not found. Run train_model.py first."
        )

    if not TEST_DIR.exists():
        raise FileNotFoundError(
            "Test dataset not found. Run data_cleaning.py first."
        )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    model = tf.keras.models.load_model(model_path)

    with open(class_path, "r") as file:
        class_names = json.load(file)

    test_data = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        class_names=class_names,
        image_size=(128, 128),
        batch_size=32,
        label_mode="int",
        shuffle=False
    )

    loss, accuracy = model.evaluate(test_data, verbose=1)

    print("\nTest Results")
    print("Test Loss:", loss)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    true_labels = np.concatenate([
        labels.numpy() for _, labels in test_data
    ])

    probabilities = model.predict(test_data, verbose=1)
    predicted_labels = np.argmax(probabilities, axis=1)

    report = classification_report(
        true_labels,
        predicted_labels,
        labels=list(range(len(class_names))),
        target_names=class_names,
        zero_division=0
    )

    print("\nClassification Report:")
    print(report)

    with open(
        REPORT_DIR / "classification_report.txt", "w"
    ) as file:
        file.write(report)

    matrix = confusion_matrix(
        true_labels,
        predicted_labels,
        labels=list(range(len(class_names)))
    )

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=class_names
    )

    display.plot(cmap="Blues", xticks_rotation=45)
    plt.title("Potato Disease CNN - Confusion Matrix")
    plt.tight_layout()
    plt.savefig(
        REPORT_DIR / "confusion_matrix.png",
        dpi=150
    )
    plt.show()

    print("\nReports saved in:", REPORT_DIR)


if __name__ == "__main__":
    test_model()
