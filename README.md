<<<<<<< HEAD
# 🥔 TuberGuard AI
### Intelligent Potato Disease Detection and Treatment Recommendation System

**Detect Early. Treat Smart. Grow Better.**

TuberGuard AI is a deep learning project that uses a Convolutional Neural Network (CNN) to identify potato diseases from uploaded leaf or plant images. It predicts the most likely disease class and provides general treatment, prevention, and fertilizer guidance through an interactive application.

The project includes image data cleaning, dataset preparation, CNN model training, model evaluation, and both Streamlit and Gradio interfaces.

## 📌 Project Overview

Potato diseases can affect crop quality and productivity. TuberGuard AI aims to help users identify possible potato diseases from images and understand basic disease-management practices.

### Key Features

- 🖼️ Upload an image for disease prediction.
- 🧠 CNN-based image classification.
- 🧹 Image validation and dataset preparation.
- 🔄 Image augmentation during model training.
- 📊 Model evaluation and classification report.
- 📉 Confusion matrix visualization.
- 🌱 General disease-management and fertilizer guidance.
- 🌐 Streamlit and Gradio user interfaces.
- 📁 Organized model files, datasets, and evaluation reports.

## 🦠 Supported Classes

The model is trained to classify images into the following seven classes:

1. Black Scurf
2. Blackleg
3. Common Scab
4. Dry Rot
5. Healthy Potatoes
6. Miscellaneous
7. Pink Rot

**Note:** The model predicts one of its trained classes. Its predictions may not always be correct, especially for images that differ from the training dataset.

## 🗂️ Project Structure

```text
TuberGuard-AI/
│
├── dataset/
│   └── potato/
│       ├── Black Scurf/
│       ├── Blackleg/
│       ├── Common Scab/
│       ├── Dry Rot/
│       ├── Healthy Potatoes/
│       ├── Miscellaneous/
│       └── Pink Rot/
│
├── processed_data/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── models/
│   ├── class_names.json
│   ├── potato_cnn.keras
│   └── potato_cnn_final.keras
│
├── reports/
│   ├── classification_report.txt
│   └── confusion_matrix.png
│
├── app.py
├── app1.py
├── data_cleaning.py
├── disease_recommendations.py
├── gradio_old.txt
├── main.py
├── test_model.py
├── train_model.py
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Deep Learning:** TensorFlow and Keras
- **Image Processing:** Pillow
- **Data Processing:** NumPy
- **Model Evaluation:** Scikit-learn
- **Web Interfaces:** Streamlit and Gradio
- **Visualization:** Matplotlib

## ⚙️ Installation

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/TuberGuard-AI.git
cd TuberGuard-AI
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 🚀 How to Run the Project

### Option 1: Streamlit Interface

Run the following command if `app1.py` is your Streamlit application:

```bash
python -m streamlit run app1.py
```

If your Streamlit application is in `app.py`, use:

```bash
python -m streamlit run app.py
```

### Option 2: Gradio Interface

Run the following command if `app.py` contains your Gradio interface:

```bash
python app.py
```

If your Gradio code is in another file, replace `app.py` with that file's name.

**Important:** `gradio_old.txt` is treated as an old backup in this project structure. If you want to run that interface, move the active Gradio code into a separate Python file, such as `gradio_app.py`. Avoid naming a Python file `gradio.py`, because it can conflict with the installed Gradio package.

## 🧹 Data Cleaning and Preparation

The `data_cleaning.py` module prepares the image dataset for training.

The data preparation workflow may include:

- Checking whether image files can be opened.
- Removing invalid images.
- Detecting duplicate images.
- Splitting images into training, validation, and testing datasets.
- Organizing images by class.

Run the data preparation script using:

```bash
python data_cleaning.py
```

Check the script to confirm that it supports direct execution before running this command. If it only defines functions, call those functions through `main.py` or another script.

## 🧠 Train the CNN Model

The `train_model.py` script trains the CNN using the prepared dataset.

The training workflow includes:

- Loading training and validation images.
- Resizing images to the model's expected input size.
- Normalizing image pixel values.
- Applying image augmentation, such as horizontal flipping, rotation, and zoom, if configured in the training script.
- Training the CNN model.
- Saving the trained model and class names.

Run:

```bash
python train_model.py
```

The trained model files are stored in the `models/` directory, depending on the paths defined in the script.

## 📊 Evaluate the Model

The `test_model.py` script evaluates the trained model using the test dataset.

Run:

```bash
python test_model.py
```

Evaluation outputs may include:

- Classification report.
- Precision, recall, and F1-score.
- Confusion matrix.

The generated reports are stored in the `reports/` directory if the script is configured to save them there.

## 🌱 Disease Recommendations

The `disease_recommendations.py` module contains general disease-management guidance associated with the predicted class.

It may provide information about:

- Recommended management practices.
- Prevention measures.
- General fertilizer guidance, where appropriate.

Recommendations should be reviewed against reliable agricultural guidance. Fertilizer alone does not cure most potato diseases, and treatment depends on the disease, crop stage, and local conditions.

## 📦 Model Files

The `models/` directory contains:

- `potato_cnn.keras` — a saved CNN model.
- `potato_cnn_final.keras` — another saved CNN model.
- `class_names.json` — class labels used by the application.

Ensure that the application loads the intended model and that `class_names.json` matches the class order used during training. The model filenames should correspond to the paths configured in your application code.

## 📋 Requirements

The project may require the following Python packages:

```text
tensorflow
numpy
pandas
Pillow
scikit-learn
matplotlib
streamlit
gradio
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

Use compatible package versions for your installed Python version. The actual `requirements.txt` file should contain the packages and versions required by your code.

## ⚠️ Limitations

- Prediction accuracy depends on the quality, diversity, and quantity of training images.
- The model can misclassify images, particularly unfamiliar images or images with multiple symptoms.
- The Miscellaneous class may contain images that do not represent a single specific disease.
- Treatment and fertilizer recommendations are general information, not a confirmed diagnosis.
- Always consult a qualified agricultural expert or local agricultural extension service for disease confirmation and treatment decisions.

## 🔮 Future Enhancements

- Improve accuracy by expanding and balancing the training dataset.
- Add more potato disease classes.
- Improve prediction confidence and error handling.
- Deploy the application online.
- Add more detailed agricultural guidance verified by experts.
- Improve the user interface and reporting features.

## 👩‍💻 Author

**Soumya Basappa Mattikoppa**  
Software Engineer
---

**TuberGuard AI — Detect Early. Treat Smart. Grow Better.**
=======
# TuberGuard-AI-potato-disease-detection-project
>>>>>>> a0d65e189c136ac27073743ed31eb9b1b7e8cc9c
