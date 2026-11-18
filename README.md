# Hand Gesture Recognition

## Project Overview
Hand Gesture Recognition is a real-time computer vision project developed using Python, OpenCV and MediaPipe.

The system uses a webcam to detect hand landmarks and identify basic hand gestures based on finger positions.

## Features
- Real-time webcam hand detection
- Hand landmark tracking
- Open Palm recognition
- Fist recognition
- Victory gesture recognition
- Pointing gesture recognition
- Thumbs Up recognition

## Technologies Used
- Python
- OpenCV
- MediaPipe
- Computer Vision

## Project Structure
```text
Hand_Gesture_Recognition/
│
├── realtime_detection.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Install Python.
2. Open the project folder in VS Code.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

```bash
python realtime_detection.py
```

Allow webcam access when prompted.

Press **Q** to close the application.

## Working Principle
1. The webcam captures live video.
2. OpenCV processes the video frames.
3. MediaPipe detects hand landmarks.
4. Finger positions are analyzed.
5. A rule-based classifier identifies the gesture.
6. The recognized gesture is displayed on the screen.

## Project Type
Real-Time Computer Vision and Rule-Based Gesture Classification.

## Internship
SkillCraft Technology – Machine Learning Internship

**Task 04: Hand Gesture Recognition**