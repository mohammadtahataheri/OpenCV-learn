# 🅿️ OpenCV Learn

### Real-Time Parking Sign Detection with Python & OpenCV

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)](https://github.com/mohammadtahataheri/OpenCV-learn)

**OpenCV Learn** is a practical computer vision project that explores real-time image processing and template matching using Python, OpenCV, and NumPy.

The current implementation uses a webcam to search for predefined parking-related signs and image patterns, then highlights detected matches with red rectangles.

> Exploring computer vision through practical experiments, one frame at a time. 🚀

---

## ✨ Features

- 📷 **Live Camera Feed** — Capture real-time video using OpenCV.
- 🅿️ **Parking Sign Matching** — Search for predefined image templates in camera frames.
- 🔍 **Template Matching** — Use `cv2.matchTemplate()` to compare image patterns.
- ⚫ **Grayscale Processing** — Convert camera frames and templates to grayscale.
- 🎯 **Similarity Threshold** — Filter matches using a configurable threshold.
- 🟥 **Visual Detection** — Draw red rectangles around detected matches.
- ⚡ **Real-Time Processing** — Continuously process incoming camera frames.

---

## 🧠 How It Works

The application follows this basic workflow:

1. **Capture:** Read a frame from the webcam.
2. **Preprocess:** Convert the camera frame to grayscale.
3. **Load Templates:** Read predefined parking-related images in grayscale.
4. **Match:** Compare each template against the camera frame using `cv2.matchTemplate()`.
5. **Filter:** Select matching locations whose scores meet the configured threshold.
6. **Visualize:** Draw red rectangles around the detected regions.
7. **Repeat:** Continue processing frames until the user exits.

### Matching Method

The project uses:

```python
cv2.matchTemplate(
    frame_gray,
    img_template,
    cv2.TM_CCOEFF_NORMED
)
```

`cv2.TM_CCOEFF_NORMED` calculates normalized correlation scores between the template and image regions.

The current threshold is:

```python
theeshhold = 0.55
```

Locations with scores greater than or equal to this value are considered matches by the current implementation.

**Note:** Template matching is not a trained object-detection model. Detection quality depends on the templates, camera conditions, image scale, and similarity threshold.

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python 3 | Application logic |
| OpenCV (`cv2`) | Camera capture, image processing, template matching, and visualization |
| NumPy | Processing template-matching results |

---

## 📋 Requirements

Before running the project, make sure you have:

- Python 3
- `pip`
- A working webcam or accessible camera device
- The required template images
- OpenCV and NumPy

---

## 🚀 Getting Started

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
python -m pip install opencv-python numpy
```

### 4. Add the Template Images

The application references the following image files:

```text
images.png
images (1).png
Free_parking_sign_cropped.jpg
Pasted image.png
download.jpeg
download1.jpeg
download2.jpeg
download3.jpeg
download4.jpeg
OIP-2000455660.jpg
OIP-2051233341.jpg
```

Place the required image files in the same directory as `main.py`, or update the paths in the `templates` list to match their actual locations.

The program skips templates that cannot be loaded, so missing image files will not be available for matching.

### 5. Run the Application

```bash
python main.py
```

The application will attempt to open camera device `0` and display the processed video in an OpenCV window.

---

## 🎮 Controls

| Key | Action |
|---|---|
| `Esc` | Exit the application |

---

## 📂 Project Structure

The current repository contains the following files:

```text
OpenCV-learn/
├── main.py
└── README.md
```

The template images are external runtime assets referenced by `main.py` and must be supplied separately unless they are added to the repository.

---

## 📚 Learning Objectives

This project provides practical experience with:

- Real-time video capture
- Grayscale image processing
- Image templates and pattern matching
- Normalized correlation
- Threshold-based match selection
- Drawing detection results on video frames
- Handling multiple image templates
- Building computer vision applications with Python

---

## 🗺️ Roadmap

Potential improvements for future versions:

- [ ] Load and cache templates before entering the main loop.
- [ ] Handle camera initialization and frame-capture failures.
- [ ] Add configurable matching thresholds.
- [ ] Reduce duplicate and overlapping detections.
- [ ] Display matching confidence scores.
- [ ] Improve detection across different image scales.
- [ ] Add a configuration file for template paths.
- [ ] Benchmark performance and optimize frame processing.
- [ ] Experiment with more robust object-detection approaches.

---

## 👨‍💻 Author

**Mohammad Taha Taheri**

- GitHub Profile: [@mohammadtahataheri](https://github.com/mohammadtahataheri)
- Repository: [OpenCV-learn](https://github.com/mohammadtahataheri/OpenCV-learn)

---

## 📄 License

Check the repository for an existing `LICENSE` file to determine the applicable licensing terms.

---

<p align="center">
  <b>Learning computer vision by building real projects. 🚀</b>
</p>
