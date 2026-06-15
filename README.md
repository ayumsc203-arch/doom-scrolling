# 📱 Real-Time Phone Detector with Audio Alert

A real-time object detection application that uses YOLOv8 to detect cell phones via webcam and plays a sound alert when one is found.

---

## 🚀 Features

- Real-time webcam feed using OpenCV
- Cell phone detection using YOLOv8 nano model
- Bounding box drawn around detected phone
- Audio alert plays when a phone is detected (no repeat until sound finishes)
- Press `ESC` to exit

---

## 🛠️ Requirements

### Python Version
Python 3.8+

### Dependencies

Install all required packages via pip:

```bash
pip install opencv-python ultralytics pygame
```

| Package | Purpose |
|---|---|
| `opencv-python` | Webcam capture and frame display |
| `ultralytics` | YOLOv8 model for object detection |
| `pygame` | Playing the audio alert |

---

## 📁 Project Structure

```
project/
│
├── phone_detector.py       # Main script
└── wow (3).wav             # Alert sound file
```

> **Note:** The YOLOv8 model file (`yolov8n.pt`) will be auto-downloaded on first run.

---

## ⚙️ Setup & Usage

1. **Clone or download** the project files.

2. **Place your `.wav` alert sound** at the path specified in the script:
   ```
   C:\Users\ayums\OneDrive\Desktop\extrapp\wow (3).wav
   ```
   Or update the path in `phone_detector.py` to match your file location:
   ```python
   pygame.mixer.music.load(r"YOUR\PATH\TO\alert.wav")
   ```

3. **Run the script:**
   ```bash
   python phone_detector.py
   ```

4. **Point your webcam** at a cell phone — a green bounding box and audio alert will trigger on detection.

5. **Press `ESC`** to quit the application.

---

## 🧠 How It Works

1. Loads the YOLOv8 nano model (`yolov8n.pt`), which is pretrained on the COCO dataset (includes `cell phone` class).
2. Captures frames from the default webcam (`VideoCapture(0)`).
3. Runs YOLO inference on each frame.
4. If a `cell phone` is detected:
   - Draws a green rectangle around it.
   - Overlays a `"Phone Detected"` label.
   - Plays the WAV alert (only if not already playing).
5. Displays the annotated frame in a window titled `"Phone Detector"`.

---

## 🔧 Customization

- **Change webcam:** Replace `cv2.VideoCapture(0)` with `cv2.VideoCapture(1)` for a secondary camera.
- **Detect other objects:** Change `"cell phone"` to any COCO class name (e.g., `"person"`, `"laptop"`, `"car"`).
- **Change alert sound:** Update the `pygame.mixer.music.load()` path to any `.wav` or `.mp3` file.

---

## 📌 Notes

- Make sure your system has a working webcam connected.
- The first run will download `yolov8n.pt` (~6 MB) automatically.
- Detection accuracy depends on lighting and camera quality.

---

## 📄 License

This project is open-source and free to use for personal and educational purposes.
