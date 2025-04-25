## 📅 ROADMAP for EyewearSense

### Phase 1: Setup & Data
- Create Python venv, install dependencies
- Collect and organize images: glasses vs. no-glasses
- Verify data balance and quality

### Phase 2: YOLOv8 Face Detection
- Load pretrained YOLOv8
- Write `detect_face.py` to output bounding boxes
- Visualize detections for validation

### Phase 3: Haar Cascade ROI Refinement
- Load Haar Cascade frontal face classifier
- Crop and refine YOLO-detected faces
- Save refined ROIs for CNN input

### Phase 4: CNN Training
- Define CNN architecture (e.g., simple 4-layer CNN)
- Train on processed ROIs
- Track loss/accuracy curves

### Phase 5: Inference Pipeline
- Chain YOLO -> Haar -> CNN in `predict.py`
- Output prediction labels and confidences

### Phase 6: Evaluation & Analysis
- Compute accuracy, precision, recall, F1
- Create confusion matrix
- Document error cases

### Phase 7: Optimization & GUI
- Experiment with data augmentation
- Prune YOLO/CNN for speed
- (Optional) Build a Tkinter or Flask interface

### Phase 8: Finalization
- Polish code and documentation
- Remove debugging artifacts
- Package project for sharing
