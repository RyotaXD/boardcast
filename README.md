# ⚡ Telegram Broadcast 

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Telethon](https://img.shields.io/badge/Telethon-Async-red?style=for-the-badge&logo=telegram&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Skrip otomasi Telegram (*Broadcast*) berbasis Python dengan sistem rotasi perangkat acak (*Fingerprint*) dan pelaporan *real-time* via Webhook.**

</div>

---

## 🌟 Fitur Unggulan

- **🛡️ Fingerprint Rotation:** Mengubah model perangkat (Samsung, Xiaomi, Pixel, dll.), versi aplikasi, serta kode bahasa global secara otomatis di setiap pesan terkirim untuk menekan risiko pembatasan/deteksi *spam*.
- **📂 File-Based Management:** Seluruh daftar grup target dipisahkan ke dalam `target_grup.txt` dan isi promosi diatur melalui `caption.txt` agar mudah dikustomisasi tanpa menyentuh kode utama.
- **🔍 Auto-Search & Join:** Fitur opsional untuk mencari grup publik berdasarkan kata kunci (*keyword*), lalu otomatis bergabung serta melakukan *mute* notifikasi.
- **📊 Webhook Reporting:** Mengirimkan ringkasan laporan hasil *broadcast* (*Loop Report*) secara otomatis ke bot Telegram pribadi setiap putaran selesai.
---

## 🛠️ Kebutuhan Sistem

Pastikan *environment* Anda telah terinstal:
- **Python** (Versi 3.8 atau terbaru)
- Pustaka pendukung (`telethon`, `rich`, `aiohttp`)

---

## 📦 Panduan Instalasi & Penggunaan

### 1. Kloning Repository
Buka terminal Anda dan jalankan perintah berikut:

```bash
git clone [https://github.com/RyotaXD/boardcast.git](https://github.com/RyotaXD/boardcast.git)
cd boardcast
pip install telethon rich aiohttp
python broadcast.py
```

---

## 📌 Cara Mendapatkan `API_ID`, `API_HASH`, & `CHAT_ID`

Panduan singkat untuk mengambil kredensial akun Telegram dan target *chat* agar *tools* ini dapat berjalan dengan lancar.

### 1️⃣ Cara Mendapatkan `API_ID` & `API_HASH`
1. Buka situs resmi Telegram di [my.telegram.org](https://my.telegram.org/) melalui *browser* HP atau PC.
2. Masukkan nomor Telegram yang aktif, lalu klik **Next**.
3. Masukkan kode konfirmasi (OTP) yang dikirimkan ke aplikasi Telegram Anda.
4. Setelah berhasil *login*, pilih menu **API development tools**.
5. Isi formulir pembuatan aplikasi (bebas, contoh nama aplikasi: `RyotaBot`, deskripsi bebas).
6. Jika sudah, klik **Create application**.
7. Anda akan langsung mendapatkan dua data penting:
   * **`api_id`** (berupa deretan angka, contoh: `29384812`)
   * **`api_hash`** (berupa kombinasi huruf dan angka acak, contoh: `a1b2c3d4e5f67890abcdef...`)
   * *Simpan kedua data ini untuk dimasukkan saat menjalankan skrip.*

---

### 2️⃣ Cara Mendapatkan `CHAT_ID` (Target Grup / Channel)
`Chat ID` digunakan sebagai target tujuan pengiriman pesan atau tempat bot beroperasi. Format ID untuk grup/channel biasanya diawali dengan tanda minus (`-100...`).

#### **Cara 1: Menggunakan Bot Telegram (Paling Mudah)**
1. Cari bot Telegram **`@MissRose_bot`** atau **`@IDBot`** di kolom pencarian Telegram.
2. Klik **Start**.
3. Jika menggunakan `@IDBot`:
   * Masukkan bot tersebut ke dalam grup atau *channel* target (pastikan bot sudah berada di dalam grup).
   * Kirim perintah `/id` di dalam grup tersebut.
   * Bot akan membalas dengan menampilkan **Chat ID** grup Anda (contoh: `-1001234567890`).
4. Jika menggunakan `@MissRose_bot`:
   * Ketik `/id` di dalam grup target, bot akan langsung memberikan informasi ID grup tersebut.

#### **Cara 2: Melalui Web Telegram (Telegram Web)**
1. Buka [web.telegram.org](https://web.telegram.org/) (disarankan versi *Telegram Web K* atau *Z*).
2. Buka grup atau *channel* target Anda melalui *browser*.
3. Perhatikan *URL* (link) di bagian *address bar browser* Anda. Link akan berbentuk seperti ini:
   `https://web.telegram.org/k/#-1001234567890`
4. Angka yang berada setelah simbol `#` (termasuk tanda minus `-` jika ada) adalah **`Chat ID`** Anda (contoh: `-1001234567890`).
