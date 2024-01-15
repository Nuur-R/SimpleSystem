import cv2
import numpy as np

# Load Haarcascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the camera (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Define the regions for left, center, and right
    left_region = [(width // 3, 0), (width // 3, height)]
    center_region = [(2 * width // 3, 0), (2 * width // 3, height)]

    # Draw bounding boxes as lines
    cv2.rectangle(frame, left_region[0], left_region[1], (255, 0, 0), 2)    # Blue for left
    cv2.rectangle(frame, center_region[0], center_region[1], (255, 0, 0), 2)  # Red for center

    # Check if faces are detected
    if len(faces) > 0:
        # Get the first face (assuming only one face in the frame)
        x, y, w, h = faces[0]

        # Calculate the center of the face
        face_center_x = x + w // 2

        # Get the width of the frame
        frame_width = frame.shape[1]

        # Define a threshold for left and right positions
        threshold = 50

        # Check if the face is on the left or right side of the frame
        if face_center_x < frame_width // 2 - threshold:
            position_text = "Left"
        elif face_center_x > frame_width // 2 + threshold:
            position_text = "Right"
        else:
            position_text = "Center"

        # Draw bounding box around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the position text on the frame
        cv2.putText(frame, f"Position: {position_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Object Tracker', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
