import cv2
import os
import numpy as np

def enroll_new_face():
    """
    Captures a face from webcam, asks for name, and stores the face image.
    """
    print("=" * 50)
    print("FACE ENROLLMENT SYSTEM")
    print("=" * 50)
    print("\nInstructions:")
    print("- Position your face in front of the camera")
    print("- Press SPACE when ready to capture")
    print("- Press ESC to cancel\n")
    
    # Load OpenCV's pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Initialize webcam
    video_capture = cv2.VideoCapture(0)
    
    if not video_capture.isOpened():
        print("Error: Could not open webcam!")
        return
    
    face_captured = False
    face_image = None
    
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
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Press SPACE to capture", (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        # Display instructions on frame
        cv2.putText(frame, "SPACE: Capture | ESC: Cancel", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('Enroll Face - Position yourself', frame)
        
        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        # Press SPACE to capture
        if key == ord(' '):
            if len(faces) == 0:
                print("No face detected! Please try again.")
            elif len(faces) > 1:
                print("Multiple faces detected! Please ensure only one person is in frame.")
            else:
                # Extract the face region
                (x, y, w, h) = faces[0]
                face_image = gray[y:y+h, x:x+w]
                face_captured = True
                print("\n✓ Face captured successfully!")
                break
        
        # Press ESC to cancel
        elif key == 27:
            print("\nEnrollment cancelled.")
            break
    
    # Release webcam
    video_capture.release()
    cv2.destroyAllWindows()
    
    if not face_captured:
        return
    
    # Ask for name
    print("\n" + "-" * 50)
    name = input("Enter the person's name: ").strip()
    
    if not name:
        print("Error: Name cannot be empty!")
        return
    
    # Create faces directory if it doesn't exist
    faces_dir = "known_faces"
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
    
    # Create a subdirectory for this person
    person_dir = os.path.join(faces_dir, name)
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
    
    # Count existing images for this person
    existing_images = len([f for f in os.listdir(person_dir) if f.endswith('.jpg')])
    
    # Save the face image
    image_path = os.path.join(person_dir, f"{name}_{existing_images + 1}.jpg")
    cv2.imwrite(image_path, face_image)
    
    print(f"\n✓ Face enrolled successfully for '{name}'!")
    print(f"✓ Saved to: {image_path}")
    print(f"✓ Total images for {name}: {existing_images + 1}")
    
    # Count total enrolled people
    total_people = len([d for d in os.listdir(faces_dir) if os.path.isdir(os.path.join(faces_dir, d))])
    print(f"✓ Total enrolled people: {total_people}")
    print("=" * 50)

if __name__ == "__main__":
    enroll_new_face()
