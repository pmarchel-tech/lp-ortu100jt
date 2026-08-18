# 🤖 Cetak Biru Alur Otomatisasi & Chatbot Better Future (ISCA)
*Redesigned: Model Frictionless Website Test + WhatsApp Verification*

Cetak biru ini diperbarui untuk menggantikan kuis chatbot ManyChat yang panjang menjadi alur pengerjaan langsung di website (*frictionless*). Ini memanfaatkan **Commitment Effect** (pengguna menyelesaikan tes 20 menit terlebih dahulu) dan **WhatsApp Verification** (menjamin nomor WhatsApp aktif/asli karena laporan dasar dikirim langsung ke WhatsApp).

---

## 📅 BAGIAN 1: ALUR INSTAGRAM & TIKTOK DMs (MANYCHAT)
ManyChat hanya bertugas sebagai **pintu masuk pertama** untuk menyaring komentar iklan dan mengarahkan prospek langsung ke website asesmen 20 menit.

*   **Trigger (Pemicu):** User memberikan komentar di postingan Instagram/TikTok Ads yang berisi kata kunci **BAKAT**.
*   **ManyChat DM Auto-Response (Node 1):**
    > *"Halo Ayah/Bunda! Senang melihat kepedulian Anda pada masa depan pendidikan anak.* 😊
    > 
    > *Tahukah Anda bahwa **87% mahasiswa di Indonesia menyesal karena salah memilih jurusan**? Tentu kita tidak ingin hal ini terjadi pada putra/putri Anda.*
    > 
    > *Kami menyediakan tes pemetaan bakat & gaya belajar lengkap selama 20 menit secara GRATIS untuk anak Anda.*
    > 
    > *Silakan klik tombol di bawah untuk mulai mengisi kuesioner langsung dari HP Anda sekarang:"*
*   **Tombol Pilihan:**
    *   `[ Mulai Tes Bakat 20 Menit (Gratis) ]` $\rightarrow$ Mengarahkan ke Tautan Website: `https://betterfuture.id/test?source=ig_comment`

---

## ⚙️ BAGIAN 2: VERIFIKASI DATA & WHATSAPP DI APLIKASI WEB (n8n / MAKE)
Begitu prospek mengklik tautan dari ManyChat, mereka masuk ke Aplikasi Web Better Future.

1.  **Pengerjaan Tes (Langkah Pertama):**
    Siswa langsung mengisi kuesioner 19-faktor Better Future secara fokus selama 20 menit langsung di browser (Tanpa registrasi/login di awal).
2.  **Formulir Lead Capture (Setelah Tes & Sebelum Rilis Hasil):**
    Begitu pertanyaan terakhir selesai dijawab, untuk memproses hasil kuis dan mengirimkan Laporan Dasar Gratis (Rp0), siswa wajib mengisi data berikut:
    *   **Nama Lengkap Anak**
    *   **Nomor WhatsApp Aktif** (PENTING: Untuk pengiriman Link Laporan Dasar).
    *   **Email Aktif**
    *   **Nama Sekolah**
    *   **Kelas / Jenjang saat ini** (Misal: 10, 11, 12 SMA/SMK).
    *   **Preferensi Rencana Kuliah:**
        - [ ] Kuliah di Indonesia (Dalam Negeri)
        - [ ] Kuliah di Luar Negeri (Study Abroad)
    *   **Ketertarikan Terhadap Informasi Beasiswa:**
        - [ ] Tertarik Beasiswa
        - [ ] Tidak Tertarik
3.  **Layar Penyelesaian (Sunk Cost & Paywall Trigger):** Setelah pertanyaan terakhir dijawab, layar website menampilkan:
    > *🎉 **Asesmen Selesai!***
    > 
    > *Laporan Dasar Anda yang mencakup **Rangkuman Kepribadian, Kekuatan Karakter, Tantangan Karakter, dan Tips Pengembangan Diri** telah dikirimkan otomatis ke WhatsApp Anda di nomor {{WhatsApp_Number}}.*
    > 
    > *Silakan periksa chat masuk dari Better Future untuk melihat hasil gratis Anda.*
    > 
    > *Bagi Anda yang ingin mengamankan pilihan jurusan kuliah Rp100 Juta+ dengan analisis lengkap 19-Halaman & bimbingan AI Counselor 24/7, silakan pilih opsi **Upgrade Premium** di bawah ini:*


---

## 💬 BAGIAN 3: ALUR PESAN WHATSAPP & UPGRADE (WABA API)
Sistem otomatisasi backend (n8n/Make terhubung ke Gateway/WABA) mendeteksi selesainya tes dan mengirim pesan pembuka ke nomor WhatsApp prospek. Ini memastikan nomor WhatsApp yang diinput adalah **nomor asli & aktif** (karena jika palsu, mereka tidak akan pernah menerima hasil laporan).

### **Pesan 1: Pengiriman Teaser & Pitching Upgrade (Otomatis)**
*   **Waktu Kirim:** 1 Menit setelah tes selesai.
*   **Pesan Chat:**
    > *"Halo Ayah/Bunda! Terima kasih sudah mendampingi putra/putrinya menyelesaikan Asesmen Better Future.* 😊
    > 
    > *Berikut adalah tautan hasil **Laporan Dasar Gratis** anak Anda (mencakup kepribadian, kekuatan, tantangan, & tips pengembangan):*
    > *[ 📑 Klik untuk Akses Laporan Dasar ]*
    > 
    > *Berdasarkan jawaban kuis, tipe kepribadian dominannya adalah **{{tipe_kepribadian}}** dengan kekuatan utama **{{kekuatan_karakter}}**.*
    > 
    > *⚠️ **PENTING UNTUK ORANG TUA:** Ini adalah ulasan umum dasar. Memilih jurusan kuliah Rp100 Juta+ berdasarkan data dasar ini masih sangat berisiko.*
    > 
    > *Bunda dapat mengamankan masa depan pendidikannya dengan membuka **Laporan Lengkap Potensi Jurusan 19 Halaman & Akses AI Counselor 24/7** secara instan di bawah ini:*
    > *[ 💳 Klik untuk Upgrade ke Laporan Lengkap ]"*

---

## 🧑‍💼 BAGIAN 4: SKENARIO TINGKAT LANJUT & PENUTUPAN KONSELOR (MANUSIA)
Jika dalam waktu **24 Jam** prospek tidak melakukan transaksi peningkatan (*upgrade*) paket berbayar, nomor tersebut akan masuk ke antrean dasbor Konselor Manusia untuk ditindaklanjuti secara personal.

### **Pesan Follow-up Konselor (Hari ke-2):**
*   **Konselor:**
    > *"Selamat pagi/siang Ayah/Bunda! Saya dengan Konselor [Nama] dari Better Future.*
    > 
    > *Kemarin saya melihat Bunda sudah mendampingi [Nama Anak] mengakses Laporan Teaser Gaya Belajar **{{gaya_belajar}}**.*
    > 
    > *Boleh saya tahu Bunda, saat ini [Nama Anak] sedang duduk di kelas berapa sekolahnya? Dan apakah saat ini ia sudah memiliki target jurusan kuliah tertentu atau masih bingung?"*

*   **Penyelesaian Keberatan (Objection Handling):**
    *   *Jika Orang Tua ragu membelanjakan Rp149k:* Konselor mengirimkan simulasi kerugian Rp100 Juta jika salah jurusan, membandingkannya dengan tes offline yang mencapai Rp1 Juta.
    *   *Jika Orang Tua meminta diskusi mendalam:* Konselor menawarkan upgrade **Paket Zoom Premium 1-on-1 bersama Psikolog HIMPSI seharga Rp250.000**.
