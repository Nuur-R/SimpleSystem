import cv2
import mediapipe as mp
import math

# Fungsi untuk menghitung jarak antara dua landmark
def calculate_distance(lm1, lm2):
    x1, y1 = lm1.x, lm1.y
    x2, y2 = lm2.x, lm2.y
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Fungsi untuk menghitung sudut antara dua landmark dan sumbu horizontal
def calculate_angle(lm1, lm2):
    x1, y1 = lm1.x, lm1.y
    x2, y2 = lm2.x, lm2.y
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mendeteksi gesture tangan
def detect_hand_gesture(image):
    # Konversi gambar ke BGR
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Mendeteksi tangan dalam gambar
    results = hands.process(image)
    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Lakukan sesuatu dengan landmarks tangan di sini
            # Contoh: Deteksi open palm
            if is_open_palm(hand_landmarks):
                print("Open Palm detected")
            # Contoh: Deteksi thumbs up
            if is_thumbs_up(hand_landmarks):
                print("Thumbs Up detected")
            # Gambar skeleton tangan
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    return image

# Fungsi untuk mendeteksi open palm
def is_open_palm(hand_landmarks):
    # Ambil landmark untuk setiap jari
    thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Hitung jarak antara ujung ibu jari dan ujung jari lainnya
    thumb_index_dist = calculate_distance(thumb, index)
    thumb_middle_dist = calculate_distance(thumb, middle)
    thumb_ring_dist = calculate_distance(thumb, ring)
    thumb_pinky_dist = calculate_distance(thumb, pinky)

    # Jika jarak antara ujung ibu jari dan ujung jari lainnya melebihi ambang batas, tangan dianggap terbuka
    threshold_distance = 0.1  # Misalnya, Anda dapat menetapkan ambang batas sesuai kebutuhan
    if (thumb_index_dist > threshold_distance and
        thumb_middle_dist > threshold_distance and
        thumb_ring_dist > threshold_distance and
        thumb_pinky_dist > threshold_distance):
        return True
    else:
        return False

# Fungsi untuk mendeteksi thumbs up
def is_thumbs_up(hand_landmarks):
    # Ambil landmark untuk jempol dan jari telunjuk
    thumb = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    # Hitung sudut antara jari telunjuk dan sumbu horizontal
    angle_threshold = 45  # Misalnya, Anda dapat menetapkan ambang batas sudut tertentu
    angle = calculate_angle(index, thumb)
    
    # Jika sudut antara jari telunjuk dan sumbu horizontal kurang dari ambang batas, dianggap thumbs up
    if angle < angle_threshold:
        return True
    else:
        return False

# Buka webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Baca frame dari webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Deteksi gesture tangan
    frame_with_detection = detect_hand_gesture(frame)
    
    # Tampilkan frame dengan skeleton tangan dan deteksi gesture
    cv2.imshow('Hand Gesture Detection', frame_with_detection)
    
    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()
