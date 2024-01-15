import cv2
import numpy as np

def detect_color(image, color_lower, color_upper):
    # Konversi frame ke format warna HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Buat mask untuk warna yang ingin dideteksi
    mask = cv2.inRange(hsv, color_lower, color_upper)
    
    # Temukan kontur dari objek yang terdeteksi
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Temukan kontur dengan luas terbesar (asumsi dot berada di tengah)
    largest_contour = max(contours, key=cv2.contourArea, default=None)
    
    # Dapatkan pusat dan warna rata-rata dari dot
    if largest_contour is not None and cv2.contourArea(largest_contour) > 0:
        moments = cv2.moments(largest_contour)
        # Pastikan momen nol tidak nol sebelum melakukan pembagian
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            color_mean = np.mean(image[cy, cx], axis=0)
            return (cx, cy), color_mean
    return None, None

def display_info(frame, center, color, label, color_code, position):
    if center is not None:
        cv2.circle(frame, center, 5, color_code, -1)  # Lingkari dot dengan warna tertentu
        cv2.putText(frame, f"{label}: {color} ({position})", (center[0] - 50, center[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_code, 2)

# Daftar warna beserta batas-batasnya
colors = [
    # {"label": "Red", "lower": np.array([0, 100, 100]), "upper": np.array([10, 255, 255]), "color_code": (0, 0, 255)},
    {"label": "Blue", "lower": np.array([100, 100, 100]), "upper": np.array([140, 255, 255]), "color_code": (255, 0, 0)},
    # {"label": "Yellow", "lower": np.array([20, 100, 100]), "upper": np.array([30, 255, 255]), "color_code": (0, 255, 255)}
]

# Inisialisasi objek VideoCapture untuk mengakses webcam
cap = cv2.VideoCapture(0)

while True:
    # Membaca frame dari webcam
    ret, frame = cap.read()

    # Mendeteksi warna untuk setiap warna dalam daftar
    for color_info in colors:
        color_lower = color_info["lower"]
        color_upper = color_info["upper"]
        center, color = detect_color(frame, color_lower, color_upper)
        
        # Menentukan posisi warna relatif terhadap lebar frame
        if center is not None:
            frame_width, _ = frame.shape[1], frame.shape[0]
            position = "Left" if center[0] < frame_width // 3 else "Center" if frame_width // 3 <= center[0] <= 2 * frame_width // 3 else "Right"
            display_info(frame, center, color, color_info["label"], color_info["color_code"], position)

    # Tampilkan frame dengan deteksi warna
    cv2.imshow('Color Detection', frame)

    # Hentikan program jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepas sumber daya webcam dan menutup jendela tampilan
cap.release()
cv2.destroyAllWindows()
