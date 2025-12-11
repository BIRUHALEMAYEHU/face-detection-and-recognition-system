# Face Detection and Recognition System

A simple webcam-based face detection and recognition tool using Python and OpenCV. Perfect for beginners!

---


how to use!

### **Step 1: Download the Code**

1. Open your terminal (Command Prompt or PowerShell on Windows)
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
   
   ✅ You'll see `(.venv)` appear at the start of your terminal line

---

### **Step 3: Install Required Software**

Run this command to install OpenCV:
```bash
pip install opencv-contrib-python
```

⏳ This will take 1-2 minutes. Wait for it to finish!

---

### **Step 4: Add Your Face**

Run the enrollment script:
```bash
python enroll_face.py
```

**What will happen:**
- Your webcam will open
- You'll see a green box around your face
- Press **SPACE** when ready
- Type your name and press **Enter**
- Done! Your face is saved

💡 **Tip:** Run this 2-3 times (different angles) for better accuracy

---

### **Step 5: Start Face Recognition**

Run the recognition script:
```bash
python recognize_faces.py
```

**What will happen:**
- Webcam opens
- **Green box** with your name appears when it recognizes you
- **Red box** with "Unknown" for people it doesn't know
- Press **'q'** to quit

---

## 🎯 Summary - Copy & Paste These Commands

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

---

## 📁 What's Inside

- `enroll_face.py` - Add new faces to the system
- `recognize_faces.py` - Real-time face recognition
- `requirements.txt` - List of required software
- `README.md` - This file!

---

## 🎓 How It Works

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

---

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

Enjoy your face recognition system! 🚀

**Quick reminder:**
- `python enroll_face.py` - Add faces
- `python recognize_faces.py` - Start recognizing
