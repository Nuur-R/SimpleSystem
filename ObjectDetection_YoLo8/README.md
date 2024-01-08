# Deteksi Objek dengan YOLOv8 Menggunakan OpenCV dan Ultralytics

Proyek ini menunjukkan contoh inferensi deteksi objek YOLOv8 menggunakan OpenCV dan Ultralytics. Proyek ini mencakup dua skrip:
- `main_webcam.py`: Melakukan inferensi YOLOv8 pada stream webcam.
- `main_mp4.py`: Melakukan inferensi YOLOv8 pada file video.

**Note :** Jika ingin memuat ulang proyek, pastikan untuk *`memuat ulang semua dependensi.`* dan ini adalah versi python dan library yg digunakan dalam pengujian.
- `python 3.9.18`
- `opencv-python 4.9.0.80`
- `ultralytics 8.0.228`

## Penggunaan

### Inferensi dengan Webcam

Jalankan perintah berikut untuk melakukan inferensi YOLOv8 pada webcam:

```bash
python main_webcam.py
```

Tekan 'q' untuk keluar dari inferensi webcam.

### Inferensi dengan File Video

Perbarui variabel `video_path` di dalam `main_mp4.py` dengan path yang benar ke file video Anda. Lalu, jalankan skrip:

```bash
python main_mp4.py
```

Tekan 'q' untuk keluar dari inferensi pada file video.

## Catatan

- Pastikan file model YOLOv8 ('models/yolov8n.pt') ada di lokasi yang benar.
- Periksa bahwa path file video benar di dalam `main_mp4.py`.
- Pastikan indeks webcam benar di dalam `main_webcam.py`.
- Perbarui dependensi jika diperlukan dengan `pip install --upgrade opencv-python ultralytics`.

## Referensi
- 📚 https://docs.ultralytics.com/modes/predict/#thread-safe-inference