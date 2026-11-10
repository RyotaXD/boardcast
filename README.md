# ⚡ Telegram Boardcast 

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telethon](https://img.shields.io/badge/Telethon-Async-red?style=for-the-badge&logo=telegram&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Skrip otomasi Telegram (*Boardcast*) berbasis Python dengan sistem rotasi perangkat acak (*Fingerprint*) dan pelaporan real-time via Webhook.**

</div>

---

## 🌟 Fitur Unggulan

- **🛡️ Dynamic Fingerprint Rotation:** Mengubah model perangkat (Samsung, Xiaomi, Pixel, dll.), versi aplikasi, serta kode bahasa global secara otomatis di setiap pesan terkirim untuk menekan risiko pembatasan/deteksi spam.
- **📂 File-Based Management:** Seluruh daftar grup target dipisahkan ke dalam `target_grup.txt` dan isi promosi diatur melalui `caption.txt` agar mudah dikustomisasi tanpa menyentuh kode utama.
- **🔍 Auto-Search & Join:** Fitur opsional untuk mencari grup publik berdasarkan kata kunci (*keyword*), lalu otomatis bergabung serta melakukan *mute* notifikasi.
- **📊 Webhook Reporting:** Mengirimkan ringkasan laporan hasil broadcast (*Loop Report*) secara otomatis ke bot Telegram pribadi setiap putaran selesai.
- **🔄 24/7 Panel Ready:** Sangat stabil dan dirancang tahan banting untuk dijalankan pada server panel otomatis seperti Pterodactyl, VPS, maupun layanan cloud lainnya.

---

## 🛠️ Kebutuhan Sistem

Pastikan environment Anda telah terinstal:
- **Python** (Versi 3.8 atau terbaru)
- Pustaka pendukung (`telethon`, `rich`, `aiohttp`)

---

## 📦 Panduan Instalasi & Penggunaan

### 1. Kloning Repository
Buka terminal Anda dan jalankan perintah berikut:
```bash
git clone https://github.com/RyotaXD/boardcast.git
cd boardcast
python build_ext --inplace
python run.py
