# OpenCV Learn 🔍

**Learning Computer Vision with Python and OpenCV.**

Welcome to **OpenCV-learn**! 🚀 This repository documents my journey into computer vision using Python, OpenCV, and NumPy through practical coding examples.

The goal is to learn image processing techniques, understand how computer vision algorithms work, and build a foundation for more advanced projects.

## 📌 Current Features

The current example demonstrates real-time edge detection using a webcam.

- 📷 **Live Webcam Feed** — Capture video from your default camera.
- 🔍 **Laplacian Edge Detection** — Detect rapid changes in image intensity.
- ➡️ **Sobel X** — Detect horizontal intensity changes.
- ⬇️ **Sobel Y** — Detect vertical intensity changes.
- 🎯 **Sobel XY** — Explore combined directional gradients.
- ⚡ **Canny Edge Detection** — Detect edges using the Canny algorithm.
- 🖥️ **Real-Time Visualization** — Display the original camera feed and processed frames in separate windows.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| OpenCV (`cv2`) | Image processing and computer vision |
| NumPy | Numerical computing and array operations |

## 📋 Requirements

Before running the project, make sure you have:

- Python 3
- A working webcam
- pip
- OpenCV
- NumPy

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mohammadtahataheri/OpenCV-learn.git
cd OpenCV-learn
```

### 2. Create a Virtual Environment (Recommended)

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install opencv-python numpy
```

### 4. Run the Project

```bash
python main.py
```

Make sure your webcam is connected and accessible before running the program.

## 🎮 Controls

- The program displays the webcam feed alongside several edge-detection outputs.
- Press **`Esc`** to exit the application.

## 📂 Project Structure

```text
OpenCV-learn/
├── main.py       # Webcam-based edge detection example
└── README.md     # Project documentation
```

## 📚 Learning Goals

This project is part of my journey toward understanding computer vision, including:

- Image processing fundamentals
- Real-time video capture
- Image gradients and edge detection
- Laplacian and Sobel operators
- Canny edge detection
- Building practical projects with Python and OpenCV

More examples and experiments may be added as the project evolves.

## 🗺️ Roadmap

- [x] Capture video from a webcam
- [x] Experiment with Laplacian edge detection
- [x] Experiment with Sobel operators
- [x] Implement Canny edge detection
- [ ] Add image loading and saving examples
- [ ] Explore color spaces and image transformations
- [ ] Experiment with contours and object detection

## 🤝 Contributions

Suggestions, bug reports, and improvements are welcome! Feel free to open an issue or submit a pull request.

## 👨‍💻 Author

**Mohammad Taha Taheri**

GitHub: [@mohammadtahataheri](https://github.com/mohammadtahataheri)

## 📄 License

No license has been specified for this repository yet. Please check the repository for licensing information before reusing or distributing its code.
