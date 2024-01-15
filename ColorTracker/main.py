import cv2
import numpy as np

colors = [
    # {"label": "Red", "lower": np.array([0, 100, 100]), "upper": np.array([10, 255, 255]), "color_code": (0, 0, 255)},
    {"label": "Blue", "lower": np.array([100, 100, 100]), "upper": np.array([140, 255, 255]), "color_code": (255, 0, 0)},
    # {"label": "Yellow", "lower": np.array([20, 100, 100]), "upper": np.array([30, 255, 255]), "color_code": (0, 255, 255)}
]

def detect_color(frame, color_data):
    # Ubah citra dari BGR ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Inisialisasi mask kosong
    mask = np.zeros_like(frame[:,:,0])  # Gunakan hanya satu channel

    # Inisialisasi variabel untuk menyimpan data dot terbaik
    best_contour = None
    best_area = 0

    # Loop melalui setiap warna
    for color_info in color_data:
        lower, upper, label, color_code = color_info["lower"], color_info["upper"], color_info["label"], color_info["color_code"]
        
        # Buat mask untuk setiap rentang warna dan tambahkan ke mask total
        color_mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        mask += color_mask

        # Temukan kontur warna yang terdeteksi
        contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop melalui setiap kontur dan simpan yang terbaik
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > best_area:
                best_contour = contour
                best_area = area

    # Gambar titik tengah dan label untuk dot terbaik
    if best_area > 500:
        M = cv2.moments(best_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            # Menentukan posisi dot di kiri, tengah, atau kanan
            width, _ = frame.shape[1], frame.shape[0]
            position = "Tengah"
            if cx < width // 3:
                position = "Kiri"
            elif cx > 2 * width // 3:
                position = "Kanan"

            cv2.circle(frame, (cx, cy), 10, color_code, -1)
            cv2.putText(frame, f"{label} - {position}", (cx - 60, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color_code, 2)

    return frame

def main():
    # Inisialisasi webcam
    cap = cv2.VideoCapture(0)

    try:
        while True:
            # Baca frame dari webcam
            ret, frame = cap.read()

            if not ret:
                print("Gagal membaca frame, pastikan webcam terhubung.")
                break

            # Deteksi warna
            result_frame = detect_color(frame, colors)

            # Tampilkan hasil
            cv2.imshow("Color Detection", result_frame)

            # Hentikan program dengan menekan tombol 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Tutup webcam dan jendela tampilan
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
