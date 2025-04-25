# 🕶️ EyewearSense
**Glasses Wearing Detection with YOLOv8, Haar Cascade & CNN**

A Python-based computer vision project for detecting eyeglasses on faces in static images using a hybrid approach: YOLOv8 for face localization, Haar Cascade for facial feature refinement, and a CNN classifier for final eyewear detection.

---

## 📋 Project Description

- **Objective**: Build an application that accurately identifies whether a person in a static image is wearing eyeglasses.
- **Methods**:
  - **YOLOv8**: Real-time face detection and bounding box generation.
  - **Haar Cascade**: Refine face ROI and detect facial landmarks.
  - **CNN**: Classify the cropped facial region as "with glasses" or "without glasses".
- **Applications**:
  - Identity verification systems
  - Security and surveillance
  - Vision assessment in healthcare

---

## 🚀 Key Features

1. **Robust Face Detection**: Leverages YOLOv8 for high-accuracy face localization.
2. **ROI Refinement**: Uses Haar Cascade to refine facial region and improve CNN performance.
3. **Deep Learning Classification**: Custom CNN distinguishes between "glasses" and "no glasses".
4. **Modular Pipeline**: Clear separation of detection, preprocessing, training, and inference.
5. **Performance Metrics**: Built-in evaluation of accuracy, precision, recall, and F1-score.

---

## 🛠️ Installation

#### 1. Clone the repository:
git clone https://github.com/username/EyewearSense.git
cd EyewearSense

#### 2. Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\\Scripts\\activate  # Windows

#### 3. Install dependencies:
pip install -r requirements.txt

#### 4. Download YOLOv8 face weights and Haar Cascade file:
# example commands
wget -P models/ https://.../yolov8_face.pt
wget -P models/ https://.../haarcascade_frontalface_default.xml

## 🎯 Usage

### Training the CNN Classifier
python src/train_cnn.py \
  --data-dir data/processed \
  --epochs 20 \
  --batch-size 32 \
  --output models/cnn_glasses.pth

## Running Inference
python src/predict.py \
  --image path/to/image.jpg \
  --yolo-weights models/yolov8_face.pt \
  --haar-cascade models/haar_cascade.xml \
  --cnn-model models/cnn_glasses.pth

## 📊 Evaluation

### After training, evaluate your model:
python src/evaluate.py \
  --test-dir data/test \
  --yolo-weights models/yolov8_face.pt \
  --haar-cascade models/haar_cascade.xml \
  --cnn-model models/cnn_glasses.pth

### Metrics reported:
Accuracy
Precision
Recall
F1-score
