# Mediapipe Hand Gesturre

## Langkah-langkah Penggunaan

### 1. Instalasi Python dan Paket Pendukung

Pastikan Anda memiliki Python terinstal di komputer Anda. Selain itu, Anda juga perlu menginstal paket `opencv-python` dan `mediapipe`. Anda dapat menginstalnya dengan menggunakan pip melalui perintah berikut di terminal atau command prompt:

```bash
pip install opencv-python
pip install mediapipe==0.10.11
```

#### 2. Persiapan Kode

Salin kode yang telah disediakan ke dalam sebuah file Python baru. Simpan file tersebut dengan nama `main.py`.

#### 3. Jalankan Kode

Jalankan file `main.py` yang telah Anda buat dengan menggunakan perintah berikut di terminal atau command prompt:

```bash
python main.py
```

Ini akan membuka feed webcam Anda dan menampilkan skeleton dari gesture tangan yang terdeteksi.

#### 4. Menggunakan Kode

Kode ini menggunakan MediaPipe untuk mendeteksi gesture tangan dan menampilkan skeletonnya dalam feed webcam. Skeleton akan ditampilkan sebagai garis-garis yang menghubungkan titik-titik landmark pada tangan.

#### 5. Interaksi

Program akan terus berjalan dan menampilkan feed webcam dengan skeleton gesture tangan hingga Anda menutup jendela atau menekan tombol 'q' pada keyboard.

### Ringkasan

Proyek ini bertujuan untuk mendeteksi gesture tangan menggunakan MediaPipe dan menampilkan skeletonnya dalam feed webcam. Anda dapat menggunakan kode ini untuk berbagai aplikasi, seperti pengendalian perangkat dengan gerakan tangan atau interaksi antarmuka pengguna berbasis gestur. Jangan ragu untuk menyesuaikan kode sesuai dengan kebutuhan Anda, seperti menambahkan logika untuk mendeteksi gesture tertentu.
