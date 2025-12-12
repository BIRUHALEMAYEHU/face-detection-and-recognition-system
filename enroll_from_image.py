import cv2
import os
import sys

def enroll_from_image():
    """
    Enroll a face from an image file.
    """
    print("=" * 50)
    print("FACE ENROLLMENT FROM IMAGE")
    print("=" * 50)
    print("\nSupported formats: .jpg, .jpeg, .png, .bmp")
    print()
    
    # Get image path from user
    image_path = input("Enter the path to the image file (or drag & drop): ").strip()
    
    # Remove quotes if user dragged and dropped
    image_path = image_path.strip('"').strip("'")
    
    # Check if file exists
    if not os.path.exists(image_path):
        print(f"\nError: File not found: {image_path}")
        return
    
    # Check file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    file_ext = os.path.splitext(image_path)[1].lower()
    if file_ext not in valid_extensions:
        print(f"\nError: Unsupported file format: {file_ext}")
        print(f"Supported formats: {', '.join(valid_extensions)}")
        return
    
    # Load the image
    print(f"\nLoading image: {os.path.basename(image_path)}")
    image = cv2.imread(image_path)
    
    if image is None:
        print("Error: Could not load image. File may be corrupted.")
        return
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces
    print("Detecting faces...")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    if len(faces) == 0:
        print("\nError: No face detected in the image!")
        print("Tips:")
        print("- Ensure the face is clearly visible")
        print("- Try a different image with better lighting")
        print("- Face should be at least 100x100 pixels")
        return
    
    # Display image with detected faces
    display_image = image.copy()
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(display_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(display_image, f"Face {i+1}", (x, y - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Show the image
    cv2.imshow('Detected Faces - Press any key to continue', display_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # If multiple faces, ask which one to use
    selected_face_idx = 0
    if len(faces) > 1:
        print(f"\n{len(faces)} faces detected in the image.")
        while True:
            try:
                selected_face_idx = int(input(f"Which face to enroll? (1-{len(faces)}): ")) - 1
                if 0 <= selected_face_idx < len(faces):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(faces)}")
            except ValueError:
                print("Please enter a valid number")
    else:
        print(f"\n✓ 1 face detected")
    
    # Extract the selected face
    (x, y, w, h) = faces[selected_face_idx]
    face_image = gray[y:y+h, x:x+w]
    
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
    output_path = os.path.join(person_dir, f"{name}_{existing_images + 1}.jpg")
    cv2.imwrite(output_path, face_image)
    
    print(f"\n✓ Face enrolled successfully for '{name}'!")
    print(f"✓ Saved to: {output_path}")
    print(f"✓ Total images for {name}: {existing_images + 1}")
    
    # Count total enrolled people
    total_people = len([d for d in os.listdir(faces_dir) if os.path.isdir(os.path.join(faces_dir, d))])
    print(f"✓ Total enrolled people: {total_people}")
    print("=" * 50)
    
    # Ask if user wants to enroll another image
    print("\nWould you like to enroll another image? (y/n): ", end="")
    if input().lower() == 'y':
        print()
        enroll_from_image()

if __name__ == "__main__":
    enroll_from_image()
