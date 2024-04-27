# Project Documentation: Face Distance Measurement

Untuk memulai menggunakan kode untuk proyek ini, Anda perlu mengikuti langkah-langkah berikut:

## Langkah 1: Instalasi Python dan Paket Pendukung

Pastikan Python telah terinstal di komputer Anda. Kemudian, Anda perlu menginstal paket OpenCV (cv2) dan mediapipe. Anda dapat menginstalnya dengan pip menggunakan perintah berikut di terminal atau command prompt:

```sh
pip install opencv-python
pip install mediapipe
```

## Langkah 2: Persiapan Kode

Salin kode yang telah disediakan ke dalam sebuah file Python baru. Simpan file tersebut dengan nama `main.py`.

## Langkah 3: Persiapan File XML

Pastikan Anda memiliki file XML untuk deteksi wajah. Kode yang disediakan menggunakan file `haarcascade_frontalface_default.xml`, yang merupakan bagian dari distribusi OpenCV. Pastikan file ini tersedia di direktori yang benar, atau sesuaikan jalur file XMLnya sesuai kebutuhan Anda.

### Langkah 4: Jalankan Kode

alankan file `main.py` yang telah Anda buat dengan perintah:

```sh
python main.py
```

Ini akan membuka feed webcam Anda dan menampilkan jarak estimasi dari wajah yang terdeteksi dalam satuan sentimeter. Jika ingin keluar dari program, cukup tekan tombol 'q' pada keyboard.

## Langkah 5: Modifikasi dan Eksperimen

Anda dapat mengubah parameter-parameter seperti `REAL_FACE_WIDTH_CM` atau `focal_length` untuk menyesuaikan dengan kamera dan kebutuhan Anda. Selain itu, Anda juga bisa melakukan eksperimen dengan kode untuk meningkatkan kinerjanya atau menyesuaikannya dengan kebutuhan spesifik Anda.

Dokumentasi ini akan membantu pengguna memahami dan menggunakan kode dengan mudah. Jangan ragu untuk menambahkan komentar di dalam kode untuk menjelaskan bagian-bagian yang kompleks atau spesifik. Semoga proyek Anda berhasil!
