# 🔍 SCOUT INTERACTIVE TOOL v10.3 (Termux Edition)

**System & Network Utility Script** berbasis Python untuk kebutuhan diagnostik jaringan, *reconnaissance*, analisis sistem, dan utilitas harian langsung di terminal Termux Android.

---

## ✨ Daftar Fitur & Menu

1. **Cek Sistem & IP Info** — Menampilkan informasi perangkat, sistem operasi, serta alamat IP lokal maupun publik.
2. **Run Network Speedtest** — Mengukur kecepatan unduh (*download*), unggah (*upload*), dan latensi (*ping*) jaringan.
3. **Target WHOIS & IP Lookup** — Melacak informasi registrasi domain, geolokasi IP, serta penyedia layanan internet (ISP).
4. **Check SSL/TLS Certificate** — Memeriksa validitas, penerbit (*issuer*), dan masa berlaku sertifikat SSL situs web.
5. **Password & API Key Generator** — Membuat kata sandi acak berkeamanan tinggi dan token API secara instan.
6. **Subdomain Finder (Recon)** — Memindai dan menemukan daftar subdomain aktif dari suatu domain target.
7. **Web Status & Header Checker** — Mengecek kode respons HTTP (`200`, `403`, `404`, dll.) beserta konfigurasi *header* server.
8. **Converter Text <-> Binary** — Mengonversi teks biasa ke kode biner dan sebaliknya.
9. **Security Port Scanner** — Memindai port terbuka (*open ports*) pada host atau IP target.
10. **Hash & Base64 Generator** — Membuat *checksum* hash (MD5, SHA256, dll.) serta melakukan *encode/decode* Base64.
11. **Background Process & RAM Analyzer** — Memantau penggunaan memori (RAM), melihat daftar proses aktif beserta PID, dan menghentikan proses tertentu.
12. **File Manager (Copy, Move, Delete)** — Mengelola file dan direktori langsung melalui antarmuka menu interaktif.

---

## 🚀 Cara Instalasi di Termux

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone [https://github.com/kangmuzz12345-droid/scout-tools.git](https://github.com/kangmuzz12345-droid/scout-tools.git)
cd scout-tools
pip install requests
