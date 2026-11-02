# 🅿️ OpenCV Learn

### Real-Time Computer Vision with Python & OpenCV

**OpenCV Learn** is a practical computer vision project built with Python, OpenCV, and NumPy. It explores real-time image processing, template matching, and camera-based detection through hands-on development.

The current implementation focuses on detecting predefined parking-related signs and patterns from a live camera feed.

The project also includes a desktop interface prototype built with CustomTkinter.

> Learning computer vision by building, experimenting, and optimizing real-world applications. 🚀

---

## ✨ Features

- 📷 **Live Camera Processing** — Capture and process video frames in real time.
- 🅿️ **Parking Sign Detection** — Search for predefined parking-related patterns.
- 🔍 **Template Matching** — Compare image regions using OpenCV's `matchTemplate()`.
- ⚫ **Grayscale Processing** — Convert frames into grayscale for template comparison.
- 🎯 **Configurable Threshold** — Control the similarity threshold for matching.
- 🟥 **Detection Visualization** — Highlight detected regions with bounding rectangles.
- ⚡ **FPS Counter** — Display approximate processing frame rate.
- 🖥️ **Desktop Interface** — Launch the application through a CustomTkinter interface.
- 🚀 **Optimized OpenCV** — Enable OpenCV's optimized processing functions.

---

## 🧠 How It Works

The current detection pipeline follows these steps:

1. **Capture:** Read frames from the camera.
2. **Preprocessing:** Convert the captured frame to grayscale.
3. **Template Loading:** Load predefined parking sign images.
4. **Matching:** Compare templates against the camera frame.
5. **Thresholding:** Filter matching locations based on similarity scores.
6. **Visualization:** Draw rectangles around detected regions.
7. **Performance Monitoring:** Calculate and display FPS.

### Template Matching

The project currently uses:

```python
cv2.matchTemplate(
    frame_gray,
    img_template,
    cv2.TM_CCOEFF_NORMED
)
```

The matching threshold is currently set to:

```python
threshold = 0.55
```

Locations with matching scores equal to or greater than the threshold are considered potential matches.

**Note:** Template matching is not a trained object detection model. Its results depend on image scale, lighting, camera conditions, template quality, and the selected threshold.

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Image processing and computer vision |
| NumPy | Numerical operations and matching results |
| CustomTkinter | Desktop graphical interface |

---

## 📋 Requirements

- Python 3
- pip
- OpenCV
- NumPy
- CustomTkinter
- A working camera device
- Required template images

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mohammadtahataheri/OpenCV-learn.git

cd OpenCV-learn
```

### 2. Create a Virtual Environment

**Linux / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install opencv-python numpy customtkinter
```

---

## 📁 Project Structure

```text
OpenCV-learn/
│
├── src/
│   ├── images.png
│   ├── images (1).png
│   ├── Free_parking_sign_cropped.jpg
│   ├── Pasted image.png
│   ├── download.jpeg
│   ├── download1.jpeg
│   ├── download2.jpeg
│   ├── download3.jpeg
│   ├── download4.jpeg
│   ├── OIP-2000455660.jpg
│   └── OIP-2051233341.jpg
│
├── launcher.py
├── main.py
└── README.md
```

The `src/` directory contains the image templates used by the detection system.

---

## ▶️ Running the Application

Start the desktop interface:

```bash
python launcher.py
```

The application launches the desktop interface and starts the camera-based detection process.

The current implementation uses camera device `0` by default.

### Controls

| Key | Action |
|---|---|
| `ESC` | Exit the camera processing window |

---

## ⚡ Performance

The project uses OpenCV's optimization support:

```python
cv2.setUseOptimized(True)
```

An FPS counter is also displayed during camera processing.

Performance depends on the camera resolution, number and size of templates, hardware, and processing conditions.

---

## 🗺️ Roadmap

Planned improvements and experiments:

- [ ] Improve frame-processing performance.
- [ ] Cache templates instead of loading them repeatedly.
- [ ] Improve camera error handling.
- [ ] Add duplicate detection filtering.
- [ ] Support multi-scale template matching.
- [ ] Add object tracking.
- [ ] Implement motion detection.
- [ ] Add image and video input support.
- [ ] Build a performance monitoring system.
- [ ] Improve the desktop interface.
- [ ] Develop a modular computer vision architecture.

---

## 🎯 Learning Objectives

This project is part of an ongoing journey into computer vision.

Main learning areas:

- Real-time video processing
- Image preprocessing
- Template matching algorithms
- Grayscale image processing
- Similarity measurement
- Camera handling with OpenCV
- Performance optimization
- Python desktop application development

---

## 👨‍💻 Author

**Mohammad Taha Taheri**

- GitHub: [@mohammadtahataheri](https://github.com/mohammadtahataheri)
- Repository: [OpenCV-learn](https://github.com/mohammadtahataheri/OpenCV-learn)

---

## 📄 License

No license file is currently included in the repository. Licensing terms have not yet been specified.

---

<p align="center">
  <b>Built with Python, OpenCV & curiosity.</b>
  <br>
  Exploring Computer Vision, one frame at a time. 🚀
</p>
