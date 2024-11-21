# **Secure RSA-DES Communication**

### **Deskripsi Proyek**
Proyek ini mengimplementasikan komunikasi aman antara server dan client menggunakan kombinasi algoritma RSA dan DES. Sistem ini mencakup:
1. Pengiriman kunci DES secara terenkripsi menggunakan algoritma RSA.
2. Public key RSA dikelola oleh Public Key Authority (PKA).
3. Pertukaran pesan antara server dan client dilakukan dalam bentuk terenkripsi menggunakan kunci DES.

Proyek bertujuan untuk mensimulasikan skenario komunikasi terenkripsi yang aman menggunakan teknik kriptografi simetris (DES) dan asimetris (RSA).

---

### **Anggota Kelompok**
1. **Nadya Zuhria Amana**  
   - **NRP:** 5025211058  
   - **Role:** Pengembangan Kode Server (`server.py`)  
2. **Dilla Wahdana**  
   - **NRP:** 502521060  
   - **Role:** Pengembangan Kode Client (`client.py`)  

---

### **Cara Menjalankan Program**

#### **Persyaratan**
- Python 3.x
- Modul Python berikut:
  - `pycryptodome` (untuk instalasi, jalankan: `pip install pycryptodome`)

#### **Langkah-Langkah**
1. **Setup Lingkungan:**
   - Pastikan Python dan modul `pycryptodome` telah terinstal.
   - Simpan file `server.py` dan `client.py` di direktori yang sesuai.

2. **Menjalankan Server:**
   - Jalankan `server.py` menggunakan perintah berikut:  
     ```bash
     python server.py
     ```
   - Server akan menampilkan public key RSA yang dihasilkan dan menunggu koneksi dari client.

3. **Menjalankan Client:**
   - Jalankan `client.py` menggunakan perintah berikut:  
     ```bash
     python client.py
     ```
   - Client akan menerima public key RSA dari server, mengenkripsi kunci DES, dan memulai komunikasi.

4. **Pertukaran Pesan:**
   - Di sisi client, masukkan pesan yang ingin dikirim ke server. Pesan akan dienkripsi dengan DES sebelum dikirim.
   - Server akan menerima pesan terenkripsi, mendekripsinya, dan dapat membalas dengan pesan yang juga dienkripsi.

5. **Mengakhiri Komunikasi:**
   - Untuk keluar, masukkan `bye` di client. Komunikasi akan dihentikan.

---

### **Pembagian Tugas**

| Nama                  | NRP       | Tugas                             |
|-----------------------|-----------|-----------------------------------|
| Nadya Zuhria Amana    | 5025211058 | Implementasi server (`server.py`) |
| Dilla Wahdana         | 502521060  | Implementasi client (`client.py`) |

---

### **Fitur Utama**
1. **RSA Key Pair Generation:**
   - Server menghasilkan public dan private key RSA.
2. **DES Key Exchange:**
   - Client mengenkripsi kunci DES menggunakan public key RSA dari server.
3. **Secure Communication:**
   - Pesan antara server dan client dienkripsi menggunakan DES dengan mode CBC.

---

### **Catatan**
- Pastikan server dan client berjalan di jaringan yang sama.
- Jalankan server terlebih dahulu sebelum client.

