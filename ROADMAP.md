# 📅 ROADMAP for EyewearSense

A structured timeline with major milestones to guide the development of the EyewearSense project.

| Phase | Timeline       | Milestones & Tasks                                  | Deliverables                     |
|-------|----------------|------------------------------------------------------|----------------------------------|
| 1     | Weeks 1 - 2    | • Environment setup and data collection              | requirements.txt, dataset folder |
|       |                | • Acquire YOLOv8 weights & Haar Cascade XML          | models/yolov8_face.pt, XML file  |
| 2     | Weeks 3 - 4    | • Develop face detection module (YOLOv8)             | src/detect_face.py               |
|       |                | • Test detection on sample images                    | detection_results/               |
| 3     | Weeks 5 - 6    | • Implement ROI refinement with Haar Cascade         | src/refine_roi.py                |
|       |                | • Integrate with YOLO outputs                        | refined_ROIs/                    |
| 4     | Weeks 7 - 8    | • Design & train CNN classifier                      | src/train_cnn.py, model weights  |
|       |                | • Hyperparameter tuning                              | training_logs/                   |
| 5     | Weeks 9 - 10   | • Build inference pipeline                           | src/predict.py                   |
|       |                | • Batch-testing on test dataset                      | test_reports/                    |
| 6     | Weeks 11 - 12  | • Evaluate performance & metrics                     | src/evaluate.py, metrics report  |
|       |                | • Analyze false positives/negatives                  | error_analysis/                  |
| 7     | Weeks 13 - 14  | • Optimize models & pipeline                         | optimized_models/                |
|       |                | • (Optional) Develop GUI or web interface            | gui/ or web_app/                 |
| 8     | Week 15        | • Final documentation & cleanup                      | README.md, ROADMAP.md            |
|       |                | • Prepare demo and presentation                      | presentation slides              |

---

## Milestone Details

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
