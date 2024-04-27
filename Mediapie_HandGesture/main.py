import cv2
import mediapipe as mp

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mendeteksi gesture tangan dan menampilkan skeleton
def detect_hand_gesture(image):
    # Mendeteksi tangan dalam gambar
    results = hands.process(image)
    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar skeleton tangan
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            # Lakukan sesuatu dengan landmarks tangan di sini
            # Anda dapat menambahkan logika untuk mendeteksi gesture tertentu
            # Misalnya, menghitung sudut antara titik-titik landmark untuk menentukan gesture
            # Lihat dokumentasi resmi MediaPipe untuk lebih lanjut: https://google.github.io/mediapipe/solutions/hands.html
    return image

# Buka webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Baca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi gesture tangan dan tampilkan skeleton
    frame_with_skeleton = detect_hand_gesture(frame)

    # Tampilkan frame dengan skeleton tangan
    cv2.imshow('Hand Gesture with Skeleton', frame_with_skeleton)

    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
