# Ujian Tengah Semester (UTS) Pemrograman Berorientasi Objek (PBO)

Repository ini berisi program Python untuk memenuhi tugas Ujian Tengah Semester (UTS) mata kuliah **Pemrograman Berorientasi Objek (PBO)**. Program yang dikerjakan mencakup dua studi kasus, yaitu sistem tagihan laundry kiloan dan sistem penggajian karyawan honorer.

## Identitas Mahasiswa

- **Nama:** [Esta Avin Nirmawan]
- **NIM:** [2695114015]
- **Kelas:** [A]
- **Program Studi:** [Teknik Informatika]

## Studi Kasus

### 1. Sistem Tagihan Laundry Kiloan

Program ini menghitung tagihan laundry berdasarkan nama pelanggan, jenis layanan, dan berat cucian. Jenis layanan yang tersedia adalah Reguler dengan tarif Rp8.000 per kilogram dan Kilat dengan tarif Rp12.000 per kilogram.

Program menghitung subtotal, diskon berdasarkan berat cucian, nominal potongan, dan total pembayaran, kemudian menampilkan nota pembayaran.

**Aturan diskon:**
- Berat minimal 10 kg: diskon 15%.
- Berat minimal 5 kg dan kurang dari 10 kg: diskon 10%.
- Berat kurang dari 5 kg: tidak mendapat diskon.

**Nama file:** `kasus_1_laundry.py`

### 2. Sistem Penggajian Karyawan Honorer

Program ini menghitung gaji mingguan karyawan berdasarkan ID karyawan, nama, dan jumlah jam kerja. Jam kerja normal dibatasi hingga 40 jam per minggu dengan tarif Rp30.000 per jam. Jam kerja di atas 40 jam dihitung sebagai lembur dengan tarif 1,5 kali tarif normal atau Rp45.000 per jam.

Program juga menghitung pajak penghasilan dan gaji bersih, kemudian menampilkan slip gaji.

**Aturan pajak:**
- Jika gaji kotor minimal Rp1.500.000, pajak sebesar 5% dari gaji kotor.
- Jika gaji kotor kurang dari Rp1.500.000, tidak dikenakan pajak.

**Rentang jam kerja yang valid:** 1–80 jam per minggu.

**Nama file:** `kasus_2_gaji.py`

## Konsep PBO yang Digunakan

Kedua program menerapkan konsep dasar Pemrograman Berorientasi Objek, meliputi:

- **Class** sebagai cetakan objek.
- **Objek** sebagai instans dari class.
- **Atribut** untuk menyimpan data.
- **Konstruktor `__init__()`** untuk menginisialisasi atribut.
- **Method** untuk menjalankan perhitungan dan menampilkan hasil.
- **Validasi input** untuk memeriksa data yang dimasukkan pengguna.

## Cara Menjalankan Program

Pastikan Python 3 telah terpasang. Buka terminal pada folder repository, lalu jalankan masing-masing program dengan perintah berikut:

```bash
python kasus_1_laundry.py
```

```bash
python kasus_2_gaji.py
```

Ikuti instruksi input yang muncul di terminal.

## Catatan Waktu Pengerjaan

- **Tanggal pengerjaan:** [19 oktober 2026]

## Tujuan

Program ini dibuat sebagai pemenuhan tugas UTS mata kuliah **Pemrograman Berorientasi Objek (PBO)** dengan menerapkan class, objek, atribut, konstruktor, method, perhitungan, dan validasi input pada dua studi kasus.