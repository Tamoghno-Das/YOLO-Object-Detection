# 🚗 Real-Time Object Detection Using YOLO

## 📌 Project Overview

This project implements **real-time object detection using YOLO (You Only Look Once)** with Python and OpenCV.

The system can detect multiple objects in **images, videos, and live webcam input**. Detected objects are displayed with bounding boxes, class names, and confidence scores.

This project is developed as part of **Module 2 – Autonomous Vehicles**, under the project topic **"Analysis of Real-Time Object Detection Using YOLO."**

---

## 🎯 Objectives

* Understand the working of YOLO-based object detection.
* Detect multiple objects in real time.
* Perform object detection on images and videos.
* Perform live object detection using a webcam.
* Display bounding boxes around detected objects.
* Display confidence scores for detected objects.
* Save the processed image with detection results.

---

## 🛠️ Technologies Used

* **Python**
* **YOLO**
* **Ultralytics**
* **OpenCV**
* **Matplotlib**

---

## 📂 Project Structure

```text
YOLO-Object-Detection/
│
├── main.py
├── requirements.txt
├── README.md
│
├── sample/
│   ├── test.jpg
│   └── traffic.mp4
│
└── output.jpg
```

---

## ⚙️ Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install ultralytics
pip install opencv-python
pip install matplotlib
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOLO-Object-Detection.git
```

### 2. Open the Project

```bash
cd YOLO-Object-Detection
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add an Input Image

Place your image inside the `sample` folder:

```text
sample/test.jpg
```

### 5. Set the Input Source

Open `main.py` and set:

```python
SOURCE = "sample/test.jpg"
```

### 6. Run the Project

```bash
python main.py
```

The YOLO model will automatically download the required model file during the first execution.

---

## 📷 Image Detection

The system processes the input image and identifies objects.

For example:

```text
Input Image
     ↓
YOLO Model
     ↓
Object Detection
     ↓
Bounding Boxes
     ↓
Class Name + Confidence
```

The processed image is saved as:

```text
output.jpg
```

---

## 🎥 Video Detection

To detect objects in a video, place a video inside the `sample` folder:

```text
sample/traffic.mp4
```

Then change:

```python
SOURCE = "sample/traffic.mp4"
```

Run:

```bash
python main.py
```

The system processes the video frame-by-frame and displays the detected objects.

Press:

```text
Q
```

to stop the video.

---

## 📹 Real-Time Webcam Detection

The project can also perform live object detection using your webcam.

Change:

```python
SOURCE = "sample/test.jpg"
```

to:

```python
SOURCE = 0
```

Then run:

```bash
python main.py
```

The webcam will open and YOLO will detect objects in real time.

Press:

```text
Q
```

to exit.

---

## 🔍 Example Detected Objects

Depending on the input, the model can detect objects such as:

* Person
* Car
* Bus
* Truck
* Bicycle
* Motorcycle
* Dog
* Cat
* Traffic-related objects
* And other supported object classes

---

## 📊 Detection Output

For every detected object, the system displays:

```text
Object: car
Confidence: 0.91

Object: person
Confidence: 0.87
```

The bounding box around each object is displayed on the image or video.

---

## 🧠 How YOLO Works

YOLO performs object detection in a single neural-network-based pipeline.

The basic process is:

```text
Input Image / Video
        ↓
YOLO Model
        ↓
Feature Extraction
        ↓
Object Detection
        ↓
Bounding Boxes
        ↓
Class Prediction
        ↓
Confidence Score
        ↓
Final Detection
```

Unlike traditional detection approaches that may process different regions separately, YOLO is designed for fast object detection and is therefore suitable for real-time applications.

---

## 🚘 Application in Autonomous Vehicles

Object detection is an important component of an autonomous vehicle perception system.

A vehicle can use object detection to identify:

* 🚗 Other vehicles
* 🧍 Pedestrians
* 🚲 Cyclists
* 🏍️ Motorcycles
* 🚌 Buses
* 🚦 Traffic-related objects

The detected information can then be used by other autonomous-driving modules for decision-making and control.

---

## 📈 Project Workflow

```text
                 Input
                   │
          ┌────────┴────────┐
          │                 │
       Image              Video
          │                 │
          └────────┬────────┘
                   ↓
              YOLO Model
                   ↓
           Object Detection
                   ↓
          ┌────────┴────────┐
          │                 │
     Class Name        Confidence
          │                 │
          └────────┬────────┘
                   ↓
            Bounding Boxes
                   ↓
              Output
```

---

## 💻 Example

Input:

```text
traffic.jpg
```

Output:

```text
Car       → 0.94
Person    → 0.89
Car       → 0.87
Bus       → 0.91
```

The detected objects are displayed directly on the image using bounding boxes.

---

## 📋 Limitations

* Detection accuracy depends on image and video quality.
* Performance can decrease in poor lighting or highly crowded scenes.
* Webcam performance depends on the computer's hardware.
* The project uses a pre-trained YOLO model and does not include custom model training.
* Detection results may vary depending on the input environment.

---

## 🔮 Future Improvements

The project can be extended by adding:

* Object tracking
* Vehicle counting
* Traffic density estimation
* Lane detection
* Traffic sign detection
* Custom YOLO model training
* Autonomous vehicle simulation
* Multi-camera detection
* Distance estimation
* Collision warning system

---

## 📚 Project Information

**Module:** Module 2 – Autonomous Vehicles

**Project:** Analysis of Real-Time Object Detection Using YOLO

**Programming Language:** Python

**Framework:** Ultralytics YOLO

**Computer Vision Library:** OpenCV

---

## 👨‍💻 Author

**Tamoghno Das**

B.Tech – Computer Science & Engineering

University of Engineering and Management, Kolkata

---

## ⭐ Conclusion

This project demonstrates how YOLO can be used for fast and practical object detection using images, videos, and live webcam input.

The project provides a simple foundation for understanding the **perception component of autonomous vehicles**, where identifying surrounding objects is an important step before decision-making and vehicle control.
