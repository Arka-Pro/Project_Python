[Terdapat gambar dengan ekstensi ".png" yang juga berfungsi sebagai panduan langsung yang telah terurut.]
[Bagian dibawah ini hanya menjelaskan lebih rinci terkait installasi dan setup Server.]

# -{Rangkuman Setup Aplikasi Server}=

# 1. Identitas

Nama       : Arka Febrian Azzavien
Kelas      : XI RPL 1
No. Absen  : 09
Tanggal    : 06 Agustus 2026

---

# 2. Aplikasi Server yang Diipilih

Saya memilih Laragon karena disarankan oleh guru saya.

---

# 3. Persiapan

Sebelum melakukan instalasi, saya menyiapkan beberapa hal berikut:

- Laptop dengan sistem operasi Windows.
- Ruang penyimpanan kosong minimal sekitar 1,22 GB sesuai keterangan pada proses instalasi.
- Pemberian Hak akses Administrator pada proses instalasi agar dapat berjalan tanpa hambatan.
- Koneksi internet untuk mengunduh file installer.
- Browser (milik saya pribadi, Brave) untuk mengecek server setelah instalasi selesai.

---

# 4. Langkah Instalasi

Berikut langkah-langkah yang saya lakukan secara berurutan:
[Anda bisa melihat gambar 2-19 sebagai referensi. ("2.png" untuk No.1, "3.png" untuk No.2, dan seterusnya...)]

1. Membuka browser dan mencari kata kunci "laragon" melalui Browser yand anda miliki untuk menemukan situs resminya.
2. Membuka situs resmi "laragon.org/download" dan mengklik [Laragon Full v8.6.1 (227 MB)] untuk  mengunduhnya (Laragon sudah menyertakan Apache, Nginx, MySQL, PHP, dan komponen pendukung lainnya dalam satu paket).
3. Menunggu proses download selesai, dan file "laragon-wamp.exe" tersimpan di folder Downloads.
4. Menjalankan file installer "laragon-wamp.exe" dengan cara double click.
5. Memilih bahasa instalasi (English) pada jendela "Select Setup Language", lalu tekan tombol [OK].
6. Menentukan lokasi instalasi pada jendela "Select Destination Location". Lokasi default yang digunakan adalah "C:\laragon", lalu tekan tombol [Next].
7. Muncul jendela "Ready to Install" yang menampilkan ringkasan konfigurasi, seperti lokasi instalasi dan informasi bahwa aplikasi nantinya bisa diakses lewat URL "https://app.test". Setelah itu tekan tombol [Install].
8. Proses instalasi berjalan (proses "Extracting files...") hingga selesai.
9. Setelah instalasi selesai, aplikasi Laragon terbuka secara otomatis dan menampilkan menu utama dengan daftar layanan Apache 2.4.66, MySQL 8.4.3, dan Mailpit 1.22.3.
10. Menekan tombol [Start All] untuk menjalankan seluruh service sekaligus (Apache dan MySQL).
11. Setelah service berhasil dijalankan, tombol yang tadinya bertuliskan "Start All" berubah menjadi [Stop], menandakan Apache dan MySQL sudah aktif.
12. Membuka browser lalu mengetikkan alamat "localhost" untuk memastikan server berjalan.
13. Halaman default Laragon berhasil tampil, menunjukkan informasi versi Apache, OpenSSL, dan PHP yang digunakan, beserta lokasi Document Root di "C:/laragon/www".
14. Membuka folder "C:\laragon\www" melalui File Explorer dan menemukan file "index.php" yang merupakan halaman default project.
15. Melakukan klik kanan pada folder project lalu memilih opsi [Open with Code] untuk membuka file tersebut di Visual Studio Code.
16. Mengedit isi file "index.php", khususnya mengganti teks judul ("h1.title") dari "Laragon" menjadi "ExampleContoh" sebagai latihan modifikasi project sederhana.
17. Menyimpan perubahan index.php, lalu me-refresh halaman "localhost" pada browser untuk melihat hasilnya.
18. Judul halaman berhasil berubah menjadi "ExampleContoh", menandakan perubahan pada file project langsung terlihat di browser.

---

# 5. Hasil Instalasi

- Laragon berhasil terinstal dengan lokasi di "C:\laragon".
- Halaman "localhost" dapat diakses melalui browser dan menampilkan informasi versi Apache, OpenSSL, serta PHP 8.3.30.
- Folder project default ("www") berisi file "index.php" yang dapat diedit dan langsung terlihat perubahannya di browser.
- Perubahan judul halaman dari "Laragon" menjadi "ExampleContoh" berhasil ditampilkan setelah file "index.php" diedit menggunakan Visual Studio Code.

---
