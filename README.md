# 🅿️ ParkVision — OpenCV Learn

### Real-Time Parking Sign Detection with Python & OpenCV

**ParkVision** is a computer vision project built with Python, OpenCV, and NumPy. It focuses on real-time camera processing and detecting predefined parking-related signs using template matching.

The project is part of my journey into computer vision, image processing, and performance optimization.

<p align="center">
  <img src="assets/Screenshot From 2026-11-11 17-29-03.png" width="700">
</p>


<p align="center">
  <img src="assets/Screenshot From 2026-11-11 17-30-39.png" width="700">
</p>


---

## ✨ Features

- 📷 **Live Camera Processing** — Capture and process frames from a camera.
- 🅿️ **Parking Sign Detection** — Detect predefined parking-related signs.
- 🔍 **Template Matching** — Use OpenCV's `matchTemplate()` method.
- ⚫ **Grayscale Processing** — Convert camera frames to grayscale for matching.
- 🎯 **Configurable Threshold** — Adjust the matching similarity threshold.
- 🟥 **Detection Visualization** — Draw bounding rectangles around detected regions.
- ⚡ **FPS Counter** — Monitor real-time processing performance.
- 🖥️ **Desktop Interface** — Launch the application through a CustomTkinter workspace.
- 🚀 **OpenCV Optimization** — Enable optimized OpenCV processing.

---

## 🧠 How It Works

ParkVision currently uses a template-matching pipeline:

1. **Camera Capture:** Read frames from the selected camera.
2. **Preprocessing:** Convert each frame to grayscale.
3. **Template Loading:** Load predefined parking sign images.
4. **Template Matching:** Compare each template against the current frame.
5. **Thresholding:** Select matching locations based on a similarity threshold.
6. **Visualization:** Draw rectangles around detected regions.
7. **Performance Monitoring:** Calculate and display FPS.

### Matching Algorithm

The project uses:

```python
cv2.matchTemplate(
    frame_gray,
    img_template,
    cv2.TM_CCOEFF_NORMED
)
```

Current matching threshold:

```python
threshold = 0.55
```

A higher threshold generally requires a stronger similarity between the template and the camera frame.

> **Note:** Template matching is not a trained object detection model. Detection quality depends on template images, scale, lighting, camera conditions, and threshold selection.

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Computer vision and image processing |
| NumPy | Numerical operations |
| CustomTkinter | Desktop graphical interface |

---

## 📋 Requirements

- Python 3.10 or newer
- pip
- OpenCV
- NumPy
- CustomTkinter
- A working camera
- Project template images

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohammadtahataheri/OpenCV-learn.git

cd OpenCV-learn
```

### 2. Create a virtual environment

**Linux / Debian / Ubuntu / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv

.venv\Scripts\activate
```

### 3. Install dependencies

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

- `main.py` — Camera processing and parking sign detection.
- `launcher.py` — CustomTkinter desktop interface.
- `src/` — Template images used by the detection system.

---

## ▶️ Running ParkVision

Start the desktop application:

```bash
python launcher.py
```

From the interface, select **View Camera** to start the camera processing window.

Press `ESC` to exit camera processing.

The current implementation uses camera device `0` by default.

---

## ⚡ Performance

Performance is an ongoing development priority.

The project uses OpenCV's optimized processing support:

```python
cv2.setUseOptimized(True)
```

An FPS counter helps observe the overall camera-processing loop.

Actual performance depends on:

- Camera resolution
- Number and dimensions of templates
- CPU performance
- Image processing workload

---

## 🗺️ Roadmap

- [x] Initial real-time camera processing
- [x] Template matching implementation
- [x] Multiple parking sign templates
- [x] CustomTkinter desktop interface
- [x] FPS monitoring
- [x] OpenCV optimization support
- [ ] Further improve frame-processing performance
- [ ] Improve camera configuration and error handling
- [ ] Reduce duplicate detection results
- [ ] Explore multi-scale template matching
- [ ] Add image and video input support
- [ ] Develop a modular computer vision architecture
- [ ] Improve desktop interface functionality

---

## 🎯 Learning Goals

This project is an ongoing learning experience focused on:

- Computer Vision
- Image Processing
- OpenCV
- Template Matching
- Real-Time Video Processing
- Performance Optimization
- Python GUI Development

---

## 👨‍💻 Author

**Mohammad Taha Taheri**

- GitHub: [@mohammadtahataheri](https://github.com/mohammadtahataheri)
- Repository: [OpenCV-learn](https://github.com/mohammadtahataheri/OpenCV-learn)

---

## 📄 License

No license file is currently specified in the repository. Licensing terms should be added when the project license is decided.

---

<p align="center">
  <b>Built with Python, OpenCV & curiosity.</b>
  <br>
  Learning Computer Vision, one frame at a time. 🚀
</p>
