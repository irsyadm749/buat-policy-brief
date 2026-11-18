# Panduan Penggunaan

Panduan ini untuk manusia, bukan untuk agen. Agen membaca `SKILL.md`; berkas ini menjelaskan
cara memakai skill dari nol, apa yang bisa diharapkan, dan kesalahan yang sering terjadi.

Versi yang dijelaskan di sini: **1.6.2**.

---

## 1. Skill ini untuk apa

Skill ini membantu menyusun dan mereviu **policy brief** dengan sistematika PerLAN, dari
posisi BPKP sebagai penyusun, untuk pembaca yang berwenang mengambil keputusan.

Tiga pekerjaan yang ditangani:

| Pekerjaan | Keluaran |
| --- | --- |
| Menyusun **outline** | Tiga bagian: Pendahuluan, Isu strategis, Arah rekomendasi |
| Menyusun **naskah lengkap** | Tujuh bagian sesuai model: Judul, Ringkasan Eksekutif, Pendahuluan, Deskripsi Masalah, Rekomendasi, Apendiks, Referensi Utama |
| **Mereviu** naskah yang sudah ada | Catatan kesesuaian penerima, kewenangan, bukti, dan kegunaan bagi keputusan |

### Yang tidak ditangani

- Mengumpulkan data. Skill menyusun, tidak mencari angka.
- Menggambar grafik atau membuat tabel dari data mentah.
- Membaca berkas .pdf atau .xlsx sebagai masukan. Untuk itu gunakan `office-transform`
  atau tempelkan isinya sebagai teks.
- Memutuskan apakah kebijakan itu baik. Skill menyusun argumen, bukan menilai kebijakan.

---

## 2. Memasang

Skill berupa folder. Salin folder ini ke direktori skill yang dibaca perkakas Anda, atau letakkan di mana pun lalu tunjuk foldernya saat meminta bantuan.

Tiga syarat yang menentukan pengenalan:

- nama folder harus `buat-policy-brief` dan sama persis dengan nilai `name:` pada frontmatter `SKILL.md`;
- berkas `SKILL.md` berada di akar folder;
- tautan rujukan memakai jalur relatif terhadap folder itu.

Beberapa lokasi yang lazim, bukan daftar lengkap: folder data aplikasi bila perkakas mengelola pustaka skill sendiri, folder `skills/` di dalam repositori kerja, atau direktori pribadi mana pun.

Bila perkakas memindai folder skill saat mulai, mulai ulang aplikasi setelah menyalin. Bila tidak ada mekanisme pemindaian, cukup sebutkan jalur folder ini saat meminta penyusunan naskah. Skill juga dapat dipakai tanpa perkakas sama sekali: buka `SKILL.md` dan ikuti isinya.

---

## 3. Cara memakai

Skill dipanggil dengan cara biasa: sebutkan pekerjaannya. Tidak perlu perintah khusus.

### Contoh untuk outline

> Buat outline policy brief tentang disparitas harga di wilayah 3T. Penerimanya Menteri
> Perdagangan. Datanya saya lampirkan berikut.

### Contoh untuk naskah lengkap

> Susun policy brief lengkap dari data ini, penerima Bupati, maksimal empat halaman.

### Contoh untuk reviu

> Reviu naskah policy brief ini. Periksa apakah keputusan yang diminta sudah jelas dan
> apakah buktinya cukup.

### Yang membuat hasil lebih baik

Empat hal ini sebaiknya disebutkan sejak awal. Kalau tidak, agen akan menebak atau bertanya.

1. **Penerima** — bupati, gubernur, Presiden, menteri, atau pimpinan lain. Ini menentukan
   bentuk rekomendasi, karena rekomendasi harus berada dalam kewenangan pembaca.
2. **Keputusan yang diminta** — satu kalimat. Apa yang pembaca diminta putuskan.
3. **Data dan sumber** — angka, periode, cakupan. Boleh tempelan teks atau lampiran.
4. **Panjang** — PerLAN memberi acuan sekitar 1.500 kata dan 2 sampai 4 halaman, dengan batas
   8 halaman. Kalau penugasan menentukan lain, sebutkan.

---

## 3a. Sebutkan tahap kebijakannya

Sejak versi 1.4.0, skill ini menanyakan satu hal lagi: **pembaca berada di tahap mana** dalam
siklus kebijakan. Alasannya, satu bentuk naskah tidak cocok untuk semua tahap.

| Tahap | Yang diputuskan pembaca | Bentuk naskah |
| --- | --- | --- |
| Penyusunan agenda | Apakah isu perlu masuk agenda | Pembuka masalah, tanpa solusi terperinci |
| Formulasi kebijakan | Pilihan mana yang diambil | Perbandingan opsi dengan kriteria |
| Penetapan kebijakan | Apakah rancangan disahkan | Ringkas, menutup keraguan terakhir |
| Pelaksanaan | Apa yang perlu diperbaiki | Hambatan pelaksanaan menjadi inti |
| Evaluasi | Dilanjutkan, diubah, atau dihentikan | Penilaian terhadap sasaran, bukan usulan baru |

Contoh menyebutkannya:

> Buat policy brief tahap **formulasi** tentang opsi pembiayaan pensertifikatan aset daerah.
> Penerimanya Bupati.

Kalau tidak disebutkan, agen akan menyimpulkannya dari keputusan yang diminta dan memberitahukannya
kepada Anda dalam satu kalimat. Anda dapat membetulkan bila keliru.

Penjelasan lengkap tiap tahap ada di `references/siklus-kebijakan.md`.

---

## 3b. Pilihan nyata dan konsekuensi sebagai dasar rekomendasi

Sejak 1.6.0, alternatif dirancang dari tujuan dan kendala keputusan sebelum menentukan rekomendasi. Setiap alternatif perlu memiliki alasan rasional untuk dipilih dan berbeda secara substantif. Paket bertingkat hanya tepat bila keputusan nyata memang menyangkut skala atau pagu.

Keadaan berjalan dianalisis sebagai baseline, termasuk biaya, risiko, kontinuitas layanan, dan biaya transisi yang dihindari. Ia tidak wajib menjadi opsi rekomendasi bila tidak sah atau tidak layak. Jelaskan alasan pengecualiannya.

Konsekuensi tetap inti: manfaat, anggaran awal dan berulang, sumber pembiayaan, belanja baru atau realokasi, biaya peluang, kapasitas pelaksanaan, risiko, pihak terdampak, dan akibat penundaan. Periksa semua alternatif dengan kriteria dan kedalaman sebanding. Data biaya belum tersedia bukan berarti nol atau buruk; nyatakan komponen, asumsi, serta kebutuhan data, tanpa mengarang nominal.

Objektivitas tidak mewajibkan kesimpulan sama kuat. Alternatif unggul boleh direkomendasikan bila bukti mendukung. Jangan menciptakan kelemahan atau kelebihan palsu untuk menyeimbangkan tabel. Bila pilihan bergantung pada kapasitas atau pagu, nyatakan syaratnya; bila bukti belum cukup, usulkan pengujian terbatas atau informasi tambahan.

Panduan kerja: [opsi dan konsekuensi](references/opsi-dan-konsekuensi.md). Dalam naskah, perbandingan tetap disampaikan lewat narasi mengalir dan tabel bila membantu, dengan nama tindakan yang konsisten.

---

## 4. Apa yang dihasilkan

### Outline

Tiga bagian, berakhir pada Arah rekomendasi. Secara bawaan **tidak** memuat Ringkasan
Eksekutif, Apendiks, Referensi Utama, Dasar Hukum, atau Sumber Data. Bagian-bagian itu
ditambahkan hanya bila diminta.

### Naskah lengkap

Tujuh bagian, dengan urutan tetap:

1. Judul
2. Ringkasan Eksekutif — ditulis terakhir, diletakkan sebelum Pendahuluan, harus dapat dibaca
   mandiri
3. Pendahuluan
4. Deskripsi Masalah
5. Rekomendasi
6. Apendiks — bila diperlukan
7. Referensi Utama

**Tentang Referensi Utama.** Bagian ini wajib pada naskah lengkap. Isinya mencampur dokumen,
instansi, periode, halaman, tautan, identitas dokumen internal, dan rujukan pasal. Subbagian
**Dasar hukum** dan **Sumber data** bukan struktur bawaan; keduanya dipakai bila penugasan
atau contoh yang diikuti memang memuatnya. Bila ingin dipisah, sebutkan sejak awal.

**Tentang tautan.** Tautan yang ditulis dalam format `[label](url)` akan menjadi hyperlink
biru yang bisa diklik setelah konversi ke .docx.

---

## 5. Keluaran berkas

Seluruh penyusunan berjalan **tanpa shell** dan hasilnya berupa teks. Konversi ke .docx
bersifat opsional dan hanya berjalan bila lingkungan menyediakan `uv`.

### Memeriksa ketersediaan

```bash
command -v uv && uv --version
```

Bila perintah tidak ditemukan, lewati bagian ini. Keluaran teks tetap sah, dan .docx dapat
dibuat manual dengan membuka Markdown di Word atau LibreOffice.

### Mengonversi

```bash
uv run --with python-docx python scripts/policy_brief_to_docx.py \
  --in naskah.md --out naskah.docx --title "Policy Brief"
```

Keluaran yang ditampilkan skrip:

```
selesai: naskah.docx
  heading         : 22
  paragraf        : 30
  butir           : 0
  bernomor        : 0
  tabel           : 2 (9 baris)
  pemisah halaman : 1
  tautan          : 10
```

Angka itu bukan hiasan. Bila tabel berisi 0 padahal naskah Anda punya tabel, ada yang gagal
dan skrip akan menulis peringatan. Baca keluarannya, jangan hanya melihat berkas jadi.

### Yang didukung konverter

Heading, paragraf rata kanan-kiri, daftar butir, daftar bernomor, tabel, tebal, miring,
tautan, dan `---` sebagai pemisah halaman. Nomor halaman ditambahkan di footer.

### Yang tidak didukung

Gambar, catatan kaki, sitasi otomatis, blockquote, dan daftar bertingkat. Bila naskah
memerlukannya, sisipkan setelah konversi di Word.

---

## 6. Yang perlu diperiksa sebelum menyerahkan

Skill menyusun, tetapi tidak menjamin. Enam hal ini perlu diperiksa manusia.

1. **Nomor halaman rujukan.** Bila naskah mengutip halaman dokumen sumber, periksa satu per
   satu. Agen dapat menulis nomor halaman yang tampak masuk akal tanpa memverifikasinya.
2. **Angka dan penyebutnya.** Pastikan setiap angka disertai periode, cakupan, dan penyebut.
   Angka tanpa penyebut mudah dipersoalkan.
3. **Kewenangan pembaca.** Rekomendasi harus dapat dijalankan penerima. Bila tidak, ubah
   menjadi usulan koordinasi atau eskalasi, bukan tindakan langsung.
4. **Klaim tentang pihak lain.** Bila naskah menyatakan suatu instansi belum melakukan
   sesuatu, pastikan sumbernya ada dan statusnya masih berlaku.
5. **Status peraturan.** Nomor dan status peraturan berubah. Verifikasi sebelum naskah
   dikirim, terutama bila peraturan dirujuk sebagai dasar kewenangan.
6. **Kesesuaian register.** Naskah untuk pimpinan bersifat padat dan formal. Jangan
   memendekkan kalimat hanya agar terdengar lebih luwes.

---

## 7. Kesalahan yang sering terjadi

**Meminta outline tetapi mengharapkan naskah lengkap.** Outline secara bawaan berhenti pada
Arah rekomendasi dan tidak memuat Referensi Utama. Sebutkan bila ingin lebih.

**Tidak menyebut penerima.** Tanpa penerima, rekomendasi menjadi umum dan tidak dapat
diputuskan siapa pun.

**Menyerahkan naskah dengan angka tanpa sumber.** Skill akan menandai ketidakpastian, tetapi
tidak akan mengarang sumber. Bila sumber belum ada, bagian itu akan terlihat kosong. Itu
disengaja.

**Mengira skill mencari data.** Skill tidak menelusuri web kecuali Anda memintanya. Bila
memang perlu, mintalah secara eksplisit, dan mintalah pemisahan yang jelas antara data
utama dan bahan pendukung.

**Mengira keluaran .docx selalu tersedia.** Tanpa `uv`, tidak. Itu bukan kerusakan.

---

## 8. Berkas di repositori ini

```
SKILL.md                        instruksi utama yang dibaca agen
PANDUAN.md                      berkas ini, untuk manusia
CHANGELOG.md                    riwayat versi dan catatan pengujian
README.md                       ringkasan repositori
scripts/
  policy_brief_to_docx.py       konversi Markdown ke .docx (opsional)
references/
  analisis-kebijakan.md         memilih metode analisis sesuai pertanyaan dan data
  model-pengawasan-bpkp.md      sistematika naskah lengkap BPKP
  penerapan.md                  contoh penerapan untuk kepala daerah dan Presiden
  pola-bahasa-id.md             daftar periksa pola bahasa yang menandai naskah mesin
  pola-contoh.md                pola narasi dari contoh policy brief
  rubrik-diklat.md              rubrik penilaian diklat, bila penugasan memerlukannya
  siklus-kebijakan.md           lima tahap siklus kebijakan dan bentuk naskah tiap tahap
```

Berkas di `references/` dibaca agen hanya saat relevan. Anda tidak perlu membacanya untuk
memakai skill, tetapi berguna bila ingin tahu dasar suatu anjuran.

---

## 9. Berkontribusi

1. Ubah berkas yang perlu diubah.
2. Naikkan `version:` pada frontmatter `SKILL.md`.
3. Catat perubahan pada `CHANGELOG.md`, termasuk **apa yang diuji dan bagaimana hasilnya**.
   Bedanya "ditambahkan" dan "diuji" penting bagi pembaca berikutnya.
4. Commit dengan pesan yang menjelaskan alasan perubahan.
5. Gunakan cabang terpisah dan merge request bila perubahan besar.

Bila mengubah `scripts/policy_brief_to_docx.py`, uji dengan naskah yang memuat tabel dan
tautan sekaligus, lalu periksa angka pada keluaran skrip. Dua kesalahan yang pernah terjadi
di skrip itu hanya terlihat saat dijalankan, tidak saat dibaca.

---

## 10. Catatan distribusi

Isi skill memuat pertimbangan internal BPKP mengenai sistematika dan register naskah. Periksa
ketentuan distribusi sebelum membagikannya ke luar unit.


## Narasi dan rujukan opsi

Penerima, tahap siklus kebijakan, keputusan yang dituju, dan sumber adalah acuan penyusunan. Jangan menjadikannya blok metadata atau narasi orang ketiga seperti "Menteri diminta memilih" atau "policy brief ini ditujukan kepada". Buka Ringkasan Eksekutif dari persoalan, akibat, dan arah perbaikan; sesuaikan kewenangan tanpa mengumumkan siapa pembacanya.

Narasi mengalir tidak berarti melarang daftar. Gunakan nomor untuk urutan langkah atau butir untuk unsur sejajar ketika lebih mudah dipindai, termasuk kalimat yang menjanjikan "lima hal berikut". Jangan menyembunyikan lima unsur itu dalam satu paragraf panjang. Hindari label mekanis per paragraf dan subbagian prosedural yang memutus argumen, tetapi pertahankan daftar yang memang membantu.

Rujuk opsi dalam narasi dengan nama tindakan singkat dan bermakna, misalnya "pemantauan yang berjalan", "standardisasi pengukuran", atau "pengukuran disertai pelaporan". Jangan mengandalkan "Pilihan A/B/C", "opsi pertama/kedua", atau "pilihan di atas" yang memaksa pembaca kembali ke tabel. Nama pada tabel dan narasi harus konsisten.
