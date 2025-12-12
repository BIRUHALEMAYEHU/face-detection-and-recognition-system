# Face Detection and Recognition System

A simple webcam-based face detection and recognition tool using Python and OpenCV. Perfect for beginners!

---

## 🚀 Quick Start Guide (For Beginners)

Follow these steps **exactly** and you'll have it working in 5 minutes!

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

**💡 Tip:** Run this 2-3 times (different angles) for better accuracy

---

### **Step 4B: Add Faces from Images (Alternative)**

If you have photos instead of a webcam, use the image enrollment script:
```bash
python enroll_from_image.py
```

**What will happen:**
- You'll be asked for an image file path
- Drag & drop an image file into the terminal (or type the path)
- The script detects faces in the image
- If multiple faces: choose which one to enroll
- Type the person's name and press **Enter**
- Done! Face is saved

**Supported formats:** `.jpg`, `.jpeg`, `.png`, `.bmp`

💡 **Tip:** You can enroll multiple images per person for better accuracy

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

# 4B. OR add face from image (alternative)
python enroll_from_image.py

# 5. Start recognition
python recognize_faces.py
```

---

## ✨ New Features

### 📸 Image Upload Enrollment

You can now enroll faces from image files instead of using the webcam!

**How to use:**
```bash
python enroll_from_image.py
```

**Features:**
- Drag & drop image files
- Supports `.jpg`, `.jpeg`, `.png`, `.bmp`
- Handles multiple faces in one image
- Visual preview of detected faces
- Batch enrollment option

### 🔄 Multi-Angle Detection

Improved face detection for better angle tolerance:
- Detects faces at slight angles (not just straight-on)
- Guides you to capture multiple angles during enrollment
- Better recognition accuracy with varied poses

**Best practice:** Enroll 3-5 images per person:
1. Looking straight
2. Head turned slightly left
3. Head turned slightly right
4. Looking slightly up
5. Looking slightly down

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

### Image enrollment: "No face detected"
- Ensure face is clearly visible in the image
- Face should be at least 80x80 pixels
- Try an image with better lighting
- Make sure the face is not too small in the photo

### Image enrollment: File not found
- Check the file path is correct
- Try dragging and dropping the file into the terminal
- Remove any extra quotes around the path

---

## 📁 What's Inside

- `enroll_face.py` - Add new faces from webcam
- `enroll_from_image.py` - Add new faces from image files
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
- `python enroll_face.py` - Add faces from webcam
- `python enroll_from_image.py` - Add faces from images
- `python recognize_faces.py` - Start recognizing
