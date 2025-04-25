# 🕶️ EyewearSense  
**Eyeglass Detection in Images Using Python and Computer Vision**

EyewearSense is a Python-based project that detects whether a person is wearing eyeglasses in static images. It uses image processing and machine learning techniques to classify faces as "with glasses" or "without glasses".

## 🚀 Features

- Detects eyeglasses in static images  
- Face detection using OpenCV or Dlib  
- Feature extraction and classification with machine learning (e.g., SVM, CNN)  
- Simple interface to test images  
- Lightweight and easy to run locally  

---

## ⚙️ Technologies Used

- Python 3.x  
- OpenCV  
- scikit-learn / TensorFlow  
- NumPy, Pandas  
- Matplotlib

---

## 📌 Roadmap

### ✅ Phase 1: Setup and Preparation
- [x] Set up Python environment  
- [x] Install required packages (`requirements.txt`)  
- [x] Collect a dataset of faces with/without glasses

### 🚧 Phase 2: Image Preprocessing
- [ ] Face detection (Haar Cascade / Dlib)  
- [ ] Crop and resize face images  
- [ ] Normalize and label the data

### 🚧 Phase 3: Model Development
- [ ] Train a simple classifier (e.g., SVM, Logistic Regression)  
- [ ] Evaluate performance  
- [ ] Try CNN-based model (optional)

### 🚧 Phase 4: Inference & Testing
- [ ] Build a test interface for single image input  
- [ ] Display prediction and confidence  
- [ ] Evaluate metrics like accuracy, precision, recall

### 🛠️ Phase 5: Optimization & Extras
- [ ] Fine-tune for better performance  
- [ ] Analyze false positives/negatives  
- [ ] (Optional) Add a basic GUI interface

---

## 📸 Sample Use

```bash
python main.py --image path/to/image.jpg
