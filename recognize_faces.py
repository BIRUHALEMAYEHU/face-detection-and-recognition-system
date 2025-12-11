import cv2
import os
import numpy as np

def load_known_faces():
    """Load all known faces from the known_faces directory."""
    faces_dir = "known_faces"
    
    if not os.path.exists(faces_dir):
        return None, None, None
    
    face_images = []
    labels = []
    label_names = {}
    current_label = 0
    
    # Iterate through each person's directory
    for person_name in os.listdir(faces_dir):
        person_dir = os.path.join(faces_dir, person_name)
        
        if not os.path.isdir(person_dir):
            continue
        
        label_names[current_label] = person_name
        
        # Load all images for this person
        for image_file in os.listdir(person_dir):
            if image_file.endswith('.jpg'):
                image_path = os.path.join(person_dir, image_file)
                face_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                
                if face_image is not None:
                    face_images.append(face_image)
                    labels.append(current_label)
        
        current_label += 1
    
    if len(face_images) == 0:
        return None, None, None
    
    return face_images, labels, label_names

def recognize_faces():
    """
    Real-time face recognition from webcam using stored face images.
    """
    print("=" * 50)
    print("FACE RECOGNITION SYSTEM")
    print("=" * 50)
    
    # Load known faces
    face_images, labels, label_names = load_known_faces()
    
    if face_images is None:
        print("\nError: No enrolled faces found!")
        print("Please run 'enroll_face.py' first to add faces.")
        return
    
    print(f"\n✓ Loaded {len(face_images)} face images")
    print(f"✓ Known people: {', '.join(label_names.values())}")
    print("\nTraining face recognizer...")
    
    # Create and train the LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(face_images, np.array(labels))
    
    print("✓ Training complete!")
    print("\nStarting webcam...")
    print("Press 'q' to quit\n")
    
    # Load OpenCV's pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize webcam
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Error: Could not open webcam!")
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        
        if not ret:
            print("Error: Failed to capture frame!")
            break
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
        
        # Recognize each detected face
        for (x, y, w, h) in faces:
            # Extract face region
            face_region = gray[y:y+h, x:x+w]
            
            # Predict the face
            label, confidence = recognizer.predict(face_region)
            
            # Lower confidence value means better match
            # LBPH confidence threshold: typically 50-70 for good matches
            if confidence < 70:
                name = label_names[label]
                # Convert confidence to percentage (inverse relationship)
                confidence_percent = max(0, 100 - confidence)
                display_name = f"{name} ({confidence_percent:.1f}%)"
                color = (0, 255, 0)  # Green for recognized
            else:
                display_name = "Unknown"
                color = (0, 0, 255)  # Red for unknown
            
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            
            # Draw label background
            label_height = 35
            cv2.rectangle(frame, (x, y + h), (x + w, y + h + label_height), color, cv2.FILLED)
            
            # Draw name
            cv2.putText(frame, display_name, (x + 6, y + h + 25),
                       cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), 1)
        
        # Display instructions
        cv2.putText(frame, "Press 'q' to quit", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('Face Recognition - Live', frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\nExiting...")
            break
    
    # Release webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()
    print("✓ Face recognition stopped.")
    print("=" * 50)

if __name__ == "__main__":
    recognize_faces()
