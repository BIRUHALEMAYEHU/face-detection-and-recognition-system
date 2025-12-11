# Face Detection and Recognition System

A simple webcam-based face detection and recognition tool using Python and OpenCV.

## Features

- ✅ Real-time face detection from webcam
- ✅ Face enrollment with name input
- ✅ Face recognition with confidence scores
- ✅ Simple file-based storage (no database required)
- ✅ Visual feedback with bounding boxes and labels
- ✅ Pure OpenCV solution (no complex dependencies)

## Installation

1. Install the required dependency:

```bash
pip install opencv-contrib-python
```

**Note:** This package includes OpenCV with extra modules including face recognition algorithms.

## Usage

### 1. Enroll New Faces

Run the enrollment script to add new faces to the system:

```bash
python enroll_face.py
```

**Instructions:**
- Position your face in front of the camera
- Press **SPACE** when ready to capture your face
- Enter your name when prompted
- Press **ESC** to cancel

You can run this script multiple times to enroll different people (5-10 people recommended).

### 2. Recognize Faces

Run the recognition script to start real-time face recognition:

```bash
python recognize_faces.py
```

**Instructions:**
- The webcam will open and start recognizing faces
- Recognized faces will be shown with **green** boxes and names
- Unknown faces will be shown with **red** boxes
- Press **'q'** to quit

## How It Works

### Face Enrollment
1. Opens webcam and detects faces using Haar Cascade
2. Captures face when SPACE is pressed
3. Asks for the person's name
4. Saves the face image to `known_faces/[name]/` directory
5. Can enroll multiple images per person for better accuracy

### Face Recognition
1. Loads all face images from `known_faces/` directory
2. Trains LBPH (Local Binary Patterns Histograms) face recognizer
3. Opens webcam and processes frames
4. Detects faces using Haar Cascade
5. Recognizes faces using trained LBPH model
6. Displays names with confidence scores

## Files

- `enroll_face.py` - Script to enroll new faces
- `recognize_faces.py` - Script for real-time face recognition
- `requirements.txt` - Python dependencies
- `known_faces/` - Directory storing face images (created after first enrollment)

## Technical Details

- **Face Detection**: Uses Haar Cascade classifier (built into OpenCV)
- **Face Recognition**: Uses LBPH (Local Binary Patterns Histograms) algorithm
- **Storage**: Face images stored in directories organized by person name
- **Matching Threshold**: 70 (lower = stricter matching)
- **Training**: Automatic on-the-fly training when recognition starts

## Troubleshooting

**Webcam not opening:**
- Check if another application is using the webcam
- Try changing camera index in code: `cv2.VideoCapture(1)` instead of `0`

**No face detected:**
- Ensure good lighting
- Position face clearly in front of camera
- Remove obstructions (glasses, masks may affect detection)

**Poor recognition accuracy:**
- Enroll multiple images of the same person (run `enroll_face.py` 2-3 times per person)
- Ensure consistent lighting during enrollment and recognition
- Adjust threshold in `recognize_faces.py` (line 92: change `< 70` to a different value)
  - Lower threshold (e.g., 60) = stricter matching, fewer false positives
  - Higher threshold (e.g., 80) = looser matching, more false positives

## Requirements

- Python 3.7+
- Webcam
- Windows/Linux/macOS

## License

Free to use for educational and personal projects.
