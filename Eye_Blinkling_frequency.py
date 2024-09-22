from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import time

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Threshold for EAR to detect blink
thresh = 0.25
blink_check = 3  # Number of consecutive frames to count as a blink
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Indices for left and right eye landmarks
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Video capture
cap = cv2.VideoCapture(0)

# Variables to store blink data
blink_counter = 0
blink_freq_per_min = 0
frame_counter = 0
start_time = time.time()

# Time interval (in seconds) to calculate blinks per minute
interval = 60  

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    
    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)
        
        # Get coordinates for eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        
        # Average EAR
        ear = (leftEAR + rightEAR) / 2.0

        # Check for blink
        if ear < thresh:
            frame_counter += 1
        else:
            if frame_counter >= blink_check:
                blink_counter += 1
            frame_counter = 0
        
        # Draw contours around eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
    
    # Calculate blink frequency per minute
    elapsed_time = time.time() - start_time
    if elapsed_time >= interval:
        blink_freq_per_min = blink_counter
        blink_counter = 0
        start_time = time.time()  # Reset the timer
    
    # Display the blink frequency
    cv2.putText(frame, f"Blinks per minute: {blink_freq_per_min}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    # Show the video feed
    cv2.imshow("Frame", frame)
    
    # Break the loop if 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release resources
cv2.destroyAllWindows()
cap.release()
