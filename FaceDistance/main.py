import cv2

# Inisialisasi Cascade Classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

# Konstanta untuk ukuran wajah dalam kondisi nyata (misalnya, 20 cm untuk lebar wajah orang dewasa rata-rata)
REAL_FACE_WIDTH_CM = 20

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Konversi ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

        # Hitung jarak menggunakan perspektif (estimasi kasar)
        focal_length = 500  # Focal length kamera (gantilah dengan focal length kamera Anda)
        image_width = frame.shape[1]

        distance_cm = (REAL_FACE_WIDTH_CM * focal_length) / w

        # Tampilkan jarak di layar
        cv2.putText(frame, f"Distance: {distance_cm:.2f} cm", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 250, 250), 2)

    # Tampilkan frame
    cv2.imshow('Face Detection', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup webcam dan jendela
cap.release()
cv2.destroyAllWindows()
