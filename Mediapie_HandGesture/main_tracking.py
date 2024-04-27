import cv2
import mediapipe as mp

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mendeteksi gesture tangan, menampilkan skeleton, dan bounding box
def detect_hand_gesture(image):
    # Mendeteksi tangan dalam gambar
    results = hands.process(image)
    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar bounding box
            x_min, y_min, x_max, y_max = calculate_bounding_box(hand_landmarks, image.shape[1], image.shape[0])
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            
            # Gambar skeleton tangan
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Lakukan sesuatu dengan landmarks tangan di sini
            # Anda dapat menambahkan logika untuk mendeteksi gesture tertentu
            # Misalnya, menghitung sudut antara titik-titik landmark untuk menentukan gesture
            # Lihat dokumentasi resmi MediaPipe untuk lebih lanjut: https://google.github.io/mediapipe/solutions/hands.html
    return image

# Fungsi untuk menghitung bounding box
def calculate_bounding_box(hand_landmarks, image_width, image_height):
    x_min, x_max = image_width, 0
    y_min, y_max = image_height, 0
    for landmark in hand_landmarks.landmark:
        x, y = int(landmark.x * image_width), int(landmark.y * image_height)
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    return x_min, y_min, x_max, y_max

# Buka webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Baca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Deteksi gesture tangan dan tampilkan skeleton serta bounding box
    frame_with_detection = detect_hand_gesture(frame)
    
    # Tampilkan frame dengan skeleton tangan dan bounding box
    cv2.imshow('Hand Gesture with Skeleton and Bounding Box', frame_with_detection)
    
    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
