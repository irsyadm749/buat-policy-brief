# Changelog

Format mengikuti [Keep a Changelog](https://keepachangelog.com/id/1.1.0/).

## [1.3.2]

### Ditambahkan
- `scripts/policy_brief_to_docx.py`: dukungan tautan Markdown `[label](url)` sebagai
  hyperlink Word berwarna biru dan bergaris bawah. Sebelumnya tautan tercetak mentah
  beserta URL-nya.
- Penghitung `tautan` pada keluaran skrip, dengan peringatan bila ada tautan yang gagal
  dibuat dan ditulis sebagai teks.
- `PANDUAN.md`: panduan penggunaan untuk manusia, mencakup cara memasang, contoh perintah,
  arti keluaran skrip, enam hal yang perlu diperiksa sebelum menyerahkan, dan kesalahan yang
  sering terjadi.

### Diperbaiki
- Pola `INLINE` memakai grup tangkap di dalam, sehingga `re.split` menyisipkan isi grup
  sebagai potongan teks dan merusak seluruh paragraf. Diganti pola tanpa grup, dengan
  ekstraksi label dan URL melalui `LINK_GROUP` terpisah.
- Pencocokan tautan memakai `match`, yang hanya berlaku di awal potongan sehingga tautan
  di tengah kalimat gagal dikenali. Diganti `fullmatch` dengan pola berjangkar.

### Diuji
Konversi dijalankan pada lingkungan Windows dengan `uv` dan `python-docx` 1.2.0, memakai
`uji-referensi.md` (4.217 karakter, 23 tautan, 1 tabel). Hasil yang terverifikasi:

- seluruh 23 tautan tampil sebagai hyperlink biru bergaris bawah di Word;
- tautan di tengah kalimat, di akhir kalimat, dan dua tautan dalam satu paragraf terbentuk;
- tautan yang bergabung dengan teks tebal terbentuk;
- tautan di dalam sel tabel terbentuk;
- struktur Referensi Utama dengan subbagian Dasar hukum dan Sumber data ter-render.

## [1.3.1]

### Diubah
- `scripts/policy_brief_to_docx.py`: mencetak hitungan hasil konversi (heading, paragraf,
  butir, bernomor, tabel, pemisah halaman) dan keluar dengan kode 3 disertai peringatan bila
  berkas masukan memuat baris berpipa tetapi tidak ada tabel yang terbentuk.

### Diuji
Konversi dijalankan pada lingkungan Windows dengan `uv` dan `python-docx` 1.2.0, memakai
naskah `policy-brief-aset-tanah.md` (12.861 karakter, 22 heading, tabel 4 kolom x 3 baris,
4 butir, 3 langkah bernomor, 1 pemisah halaman). Hasil yang terverifikasi:

- tabel terbentuk sebagai tabel bergaris, bukan teks berpipa;
- teks di dalam sel tidak berganda;
- nomor halaman pada footer tampil sebagai angka;
- daftar butir dan daftar bernomor memakai gaya bawaan Word.

## [1.3.0]

### Ditambahkan
- `scripts/policy_brief_to_docx.py`: konversi Markdown ke .docx memakai python-docx.
  Opsional dan tidak diperlukan untuk menyusun naskah.
- `SKILL.md`: bagian "Keluaran berkas (opsional)" yang memeriksa ketersediaan `uv`
  lebih dahulu dan menyatakan bahwa keluaran teks tetap sah bila shell tidak tersedia.

### Catatan
- Bagian prosa tetap mandiri. Tanpa `uv`, seluruh alur penyusunan naskah berjalan
  seperti sebelumnya; hanya konversi .docx yang tidak tersedia.

## [1.2.0]

### Diubah
- `references/pola-bahasa-id.md` disusun ulang berdasarkan dua naskah pembanding:
  Catatan Kebijakan PSKK UGM No. 2/Oktober/2026 dan sebuah policy brief 10 halaman tentang
  tata kelola PPYBB.
- Tambah gerbang register di awal berkas: naskah formal tidak dipendekkan, hanya kalimat yang
  tidak menambah fakta yang dibuang.
- Pola "deret tiga yang dipaksakan" diperluas menjadi "daftar yang lebih panjang daripada bukti".
- Pola nominalisasi diberi uji: konsep yang dianalisis dibiarkan, pemanis dipotong.
- Hapus tanda pisah panjang dan huruf tebal dari daftar sasaran.
- Tambah anafora struktural dan bagian pemeriksaan mekanis.

## [1.1.0]

### Ditambahkan
- `references/pola-bahasa-id.md`: daftar periksa pola bahasa Indonesia yang menandai naskah
  mesin.

### Diubah
- `SKILL.md`: instruksi "Baca ulang untuk merapikan pola kalimat" merujuk daftar periksa
  tersebut.

## [1.0.0]

### Ditambahkan
- Versi awal: `SKILL.md` dan lima berkas rujukan.
