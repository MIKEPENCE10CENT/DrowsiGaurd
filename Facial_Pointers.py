import cv2
import dlib
import numpy as np

# Load face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        # Draw landmarks on the face
        for i in range(68):
            x, y = landmarks.part(i).x, landmarks.part(i).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)  # Red color in BGR format

        # Optionally, draw lines between specific landmarks
        # Example: Draw lines between eyes and mouth points for visualization
        # Eyebrows
        cv2.line(frame, (landmarks.part(22).x, landmarks.part(22).y), (landmarks.part(23).x, landmarks.part(23).y), (0, 0, 255), 1)
        cv2.line(frame, (landmarks.part(21).x, landmarks.part(21).y), (landmarks.part(24).x, landmarks.part(24).y), (0, 0, 255), 1)
        
        # Eyes
        cv2.line(frame, (landmarks.part(36).x, landmarks.part(36).y), (landmarks.part(39).x, landmarks.part(39).y), (0, 0, 255), 1)
        cv2.line(frame, (landmarks.part(42).x, landmarks.part(42).y), (landmarks.part(45).x, landmarks.part(45).y), (0, 0, 255), 1)
        
        # Mouth
        for i in range(48, 68):
            cv2.line(frame, (landmarks.part(i).x, landmarks.part(i).y), (landmarks.part((i + 1) % 20 + 48).x, landmarks.part((i + 1) % 20 + 48).y), (0, 0, 255), 1)

    # Display the frame
    cv2.imshow("Facial Landmarks", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
