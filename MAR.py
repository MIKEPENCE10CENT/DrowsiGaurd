import cv2
import dlib
import numpy as np
from scipy.spatial import distance

# Function to calculate the Mouth Aspect Ratio (MAR)
def calculate_mar(mouth_landmarks):
    # Ensure landmarks are within bounds
    if len(mouth_landmarks) < 20:
        raise ValueError("Insufficient number of landmarks for MAR calculation")
    
    # Example indices for mouth landmarks
    try:
        A = distance.euclidean(mouth_landmarks[3], mouth_landmarks[9])  # Example indices
        B = distance.euclidean(mouth_landmarks[2], mouth_landmarks[10]) # Example indices
        C = distance.euclidean(mouth_landmarks[4], mouth_landmarks[8])  # Example indices
        D = distance.euclidean(mouth_landmarks[0], mouth_landmarks[6])  # Example indices
        
        mar = (A + B + C) / (3.0 * D)
    except IndexError as e:
        print(f"IndexError: {e}")
        mar = 0.0  # Default value in case of error
    return mar

# Load face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)
yawn_threshold = 0.6  # Experimentally determined
yawn_count = 0
frame_yawn_duration = 15  # Number of consecutive frames with MAR > threshold to consider as a yawn

yawn_frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray, face)
        # Extract mouth points (indices 48-67 are typical for the mouth region)
        mouth_points = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 68)])
        
        try:
            mar = calculate_mar(mouth_points)
        except ValueError as e:
            print(f"ValueError: {e}")
            mar = 0.0  # Default value in case of error
        
        if mar > yawn_threshold:
            yawn_frame_counter += 1
        else:
            if yawn_frame_counter >= frame_yawn_duration:
                yawn_count += 1
            yawn_frame_counter = 0
        
        # Draw landmarks on the mouth
        for (x, y) in mouth_points:
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)  # Red color in BGR format
        
        # Optionally, draw lines between mouth points (to visualize mouth contour)
        for i in range(len(mouth_points) - 1):
            cv2.line(frame, (mouth_points[i][0], mouth_points[i][1]), (mouth_points[i + 1][0], mouth_points[i + 1][1]), (0, 0, 255), 1)

        # Display Yawn Count
        cv2.putText(frame, f"Yawn Count per minute : {yawn_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Yawning Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
