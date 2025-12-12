# Face Detection and Recognition System

A simple webcam-based face detection and recognition tool using Python and OpenCV.

how to use!

### **Step 1: Download the Code**

1. Open your terminal
2. Navigate to where you want to save the project:
   ```bash
   cd Desktop
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/BIRUHALEMAYEHU/face-detection-and-recognition-system.git
   ```
4. Go into the project folder:
   ```bash
   cd face-detection-and-recognition-system
   ```
---

### **Step 2: Set Up Python Environment**

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:
   
   **On Windows:**
   ```bash
   .venv\Scripts\activate
   ```
   
   **On Mac/Linux:**
   ```bash
   source .venv/bin/activate
   ```
   
 `(.venv)` appear at the start of your terminal line

---

### **Step 3: Install Required Software**

```bash
pip install opencv-contrib-python
```
1 - 2 min wait

---
to Add Your Face**

Run
```bash
python enroll_face.py
```
webcam will open
Press **SPACE** when ready
- Type your name and press **Enter**
- Done! Your face is saved
do it multiple times for better accuracy , also run again whenever you want to register a new user
---
**Step 5: Start Face Recognition**

Run
```bash
python recognize_faces.py
```

**What will happen:**
- Webcam opens
- **Green box** with your name appears when it recognizes you
- **Red box** with "Unknown" for people it doesn't know
- Press **'q'** to quit

---

all needed commands one by one

```bash
# 1. Download the code
git clone https://github.com/BIRUHALEMAYEHU/face-detection-and-recognition-system.git
cd face-detection-and-recognition-system

# 2. Set up environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac/Linux

# 3. Install software
pip install opencv-contrib-python

# 4. Add your face
python enroll_face.py

# 5. Start recognition
python recognize_faces.py
```

---

## ❓ Troubleshooting

### "python is not recognized"
- Install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### "No module named 'cv2'"
- Make sure your virtual environment is activated (you should see `(.venv)`)
- Run: `pip install opencv-contrib-python`

### "No webcam detected"
- Make sure your webcam is connected
- Close other apps using the webcam (Zoom, Teams, etc.)

### "No face detected"
- Ensure good lighting
- Face the camera directly
- Remove obstructions (hats, masks)

### Recognition not accurate
- Enroll 2-3 images per person: run `python enroll_face.py` multiple times
- Ensure consistent lighting



## 🔧 Technical Details

- **Face Detection**: Haar Cascade classifier (built into OpenCV)
- **Face Recognition**: LBPH (Local Binary Patterns Histograms) algorithm
- **Storage**: Face images stored in directories organized by person name
- **Matching Threshold**: 70 (lower = stricter matching)
- **Training**: Automatic on-the-fly training when recognition starts

---

## 📝 Requirements

- Python 3.7 or higher
- Webcam
- Windows/Mac/Linux

---

## 🤝 Need Help?

If you get stuck:
1. Read the error message carefully
2. Check the Troubleshooting section above
3. Make sure you followed all steps in order
4. Google the error message

---

## 📜 License

Free to use for educational and personal projects.

---

## 🎉 You're All Set!

Enjoy your face recognition system! 
