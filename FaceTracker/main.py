import cv2
import numpy as np

def detect_face(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    return faces

def determine_position(frame_width, face_center_x, threshold):
    if face_center_x < frame_width // 2 - threshold:
        return "Left"
    elif face_center_x > frame_width // 2 + threshold:
        return "Right"
    else:
        return "Center"

def draw_regions(frame, left_region, center_region):
    cv2.rectangle(frame, left_region[0], left_region[1], (255, 0, 0), 2)    # Blue for left
    cv2.rectangle(frame, center_region[0], center_region[1], (255, 0, 0), 2)  # Red for center

def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape
        left_region = [(width // 3, 0), (width // 3, height)]
        center_region = [(2 * width // 3, 0), (2 * width // 3, height)]

        draw_regions(frame, left_region, center_region)

        faces = detect_face(frame, face_cascade)

        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_center_x = x + w // 2
            frame_width = frame.shape[1]
            threshold = 50

            position_text = determine_position(frame_width, face_center_x, threshold)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Position: {position_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Object Tracker', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
