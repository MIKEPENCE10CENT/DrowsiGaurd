import cv2
import dlib
import numpy as np
import math

# Initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # Make sure to have this file

# Function to calculate head tilt angle
def calculate_head_tilt(eye_left, eye_right):
    delta_y = eye_right[1] - eye_left[1]
    delta_x = eye_right[0] - eye_left[0]
    
    # Prevent division by zero error
    if delta_x == 0:
        delta_x = 0.001
        
    # Calculate slope
    slope = delta_y / delta_x
    
    # Calculate angle in degrees
    angle = np.arctan(slope) * (180 / np.pi)
    
    return angle

# Open the default camera
cap = cv2.VideoCapture(0)

tilt_threshold = 15  # Set the tilt threshold in degrees

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        
        # Get the left and right eye centers (averaging key points)
        left_eye_center = np.mean([(landmarks.part(36).x, landmarks.part(36).y), 
                                   (landmarks.part(39).x, landmarks.part(39).y)], axis=0)

        right_eye_center = np.mean([(landmarks.part(42).x, landmarks.part(42).y), 
                                    (landmarks.part(45).x, landmarks.part(45).y)], axis=0)

        # Calculate head tilt angle
        head_tilt_angle = calculate_head_tilt(left_eye_center, right_eye_center)
        
        # Display the head tilt angle on the frame
        cv2.putText(frame, f"Tilt Angle: {head_tilt_angle:.2f} degrees", (30, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Check if head tilt exceeds the threshold
        if abs(head_tilt_angle) > tilt_threshold:
            cv2.putText(frame, "Head Tilt Detected!", (30, 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Optional: Draw landmarks (for debugging)
        for n in range(36, 48):  # Eyes landmarks
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

    # Show the video frame with tilt information
    cv2.imshow("Head Tilt Detection", frame)
    
    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
