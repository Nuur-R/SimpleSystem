import cv2
import requests
import numpy as np

# Replace with the IP address of your ESP32-CAM
esp32_cam_ip = "192.168.1.67"

# MJPEG stream URL
stream_url = f"http://{esp32_cam_ip}/"

# Open a connection to the MJPEG stream
response = requests.get(stream_url, stream=True)
bytes = bytes()

# Read MJPEG stream
for chunk in response.iter_content(chunk_size=1024):
    bytes += chunk
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b + 2]
        bytes = bytes[b + 2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('ESP32-CAM Stream', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
