import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('models/yolov8n.pt')

# Open the webcam
cap = cv2.VideoCapture(2)  # 0 corresponds to the default webcam device, you can change it if needed

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the webcam
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if there's an issue reading frames from the webcam
        break

# Release the webcam capture object and close the display window
cap.release()
cv2.destroyAllWindows()
