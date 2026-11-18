# buat-policy-brief

Skill penyusunan policy brief dengan sistematika PerLAN, disusun dari posisi BPKP sebagai penyusun naskah untuk pembaca yang berwenang mengambil keputusan.

Versi saat ini: **1.7.0**. Lihat [CHANGELOG.md](CHANGELOG.md) untuk riwayat perubahan.

Berkas ini mengikuti spesifikasi Agent Skills: satu folder berisi `SKILL.md` dengan frontmatter YAML, ditambah berkas rujukan dan skrip pendukung. Karena itu skill dapat dipakai pada berbagai perkakas yang membaca format tersebut, bukan terikat pada satu aplikasi tertentu. Isi instruksinya berupa bahasa alami, sehingga tetap dapat dibaca dan diikuti langsung oleh manusia tanpa perkakas apa pun.

## Untuk pengguna baru

Mulai dari [PANDUAN.md](PANDUAN.md). Berkas itu menjelaskan cara memakai skill dari nol, termasuk contoh perintah, contoh keluaran, dan kesalahan yang sering terjadi. README ini ringkasan isi repositori.

## Isi repositori

```
SKILL.md                        instruksi utama yang dibaca model
PANDUAN.md                      panduan penggunaan untuk manusia
CHANGELOG.md                    riwayat versi dan catatan pengujian
README.md                       berkas ini
scripts/
  policy_brief_to_docx.py       konversi Markdown ke .docx (opsional, butuh uv)
references/
  analisis-kebijakan.md         panduan memilih metode analisis
  model-pengawasan-bpkp.md      model naskah policy brief lengkap
  opsi-dan-konsekuensi.md       perancangan alternatif dan penilaian konsekuensi
  penerapan.md                  contoh penerapan untuk kepala daerah dan Presiden
  pola-bahasa-id.md             daftar periksa pola bahasa yang menandai naskah mesin
  pola-contoh.md                pola narasi dari contoh policy brief
  ringkas-dan-helicopter-view.md  concise view dan helicopter view untuk naskah kepada Presiden
  rubrik-diklat.md              rubrik penilaian diklat, bila penugasan memerlukannya
  siklus-kebijakan.md           lima tahap siklus kebijakan dan bentuk naskah tiap tahap
```

## Memasang

Skill berupa folder. Salin folder ini ke direktori skill yang dibaca perkakas Anda, atau tempatkan di mana pun lalu tunjuk foldernya. Yang menentukan pengenalan adalah:

- nama folder harus `buat-policy-brief` dan sama persis dengan nilai `name:` pada frontmatter `SKILL.md`;
- berkas `SKILL.md` berada di akar folder;
- semua tautan rujukan memakai jalur relatif terhadap folder itu.

Beberapa contoh lokasi yang lazim, bukan daftar lengkap:

| Lingkungan | Lokasi yang umum dipakai |
| --- | --- |
| Perkakas agen dengan pustaka skill terkelola | folder data aplikasi, subfolder berisi kumpulan skill |
| Penggunaan berbasis proyek | dalam repositori kerja, misalnya `skills/buat-policy-brief/` |
| Penggunaan pribadi berbasis berkas | direktori mana pun yang dapat dibaca model atau pengguna |

Bila perkakas memindai folder skill saat mulai, mulai ulang aplikasi setelah menyalin. Bila tidak ada mekanisme pemindaian, cukup sebutkan jalur folder ini saat meminta bantuan penyusunan naskah.

Berkas panduan pada `PANDUAN.md` memuat contoh perintah yang dapat dipakai pada perkakas apa pun.

## Dua cara memakai

**Hanya prosa, tanpa shell.** Seluruh alur penyusunan naskah berjalan tanpa program apa pun. Model membaca `SKILL.md` dan berkas rujukan, lalu menghasilkan naskah. Cara ini tidak memerlukan pemasangan, tidak memerlukan Python, dan tetap sah walaupun naskah akhirnya disalin manual ke pengolah kata.

**Dengan konversi .docx.** Bila lingkungan menyediakan `uv`, naskah Markdown dapat dikonversi menjadi .docx yang dapat diedit di Word. Skripnya berdiri sendiri dan hanya memerlukan `python-docx`; ia tidak bergantung pada aplikasi tertentu. Lihat bagian "Keluaran berkas" pada [PANDUAN.md](PANDUAN.md).

Keduanya tidak saling bergantung: ketiadaan `uv` bukan kerusakan, dan kehadirannya bukan syarat.

## Memperbarui

```bash
git pull
```

Lalu salin ulang folder ke direktori skill yang dipakai, atau buat tautan simbolik sekali agar setiap `git pull` langsung terpakai. Contoh pada Windows:

```powershell
New-Item -ItemType SymbolicLink `
  -Path "<folder-skill-anda>\buat-policy-brief" `
  -Target "<lokasi-repo>\buat-policy-brief"
```

Pada sistem lain, gunakan `ln -s` dengan maksud yang sama. Perlu diketahui: dengan tautan, perubahan yang dilakukan melalui aplikasi akan langsung menulis ke folder repositori, sehingga tampil sebagai perubahan yang belum di-commit. Tanpa tautan, penyalinan dilakukan manual.

## Berkontribusi

1. Ubah berkas di folder ini.
2. Naikkan `version:` pada frontmatter `SKILL.md` bila isi berubah.
3. Catat perubahan pada `CHANGELOG.md`, termasuk apa yang diuji dan bagaimana hasilnya.
4. Commit dengan pesan yang menjelaskan alasan perubahan, bukan hanya nama berkasnya.
5. Gunakan cabang terpisah dan merge request bila perubahan besar.

## Perancangan rekomendasi

Alternatif nyata, pemeriksaan yang adil, dan perbandingan konsekuensi terutama anggaran menjadi dasar rekomendasi. Lihat [panduan opsi dan konsekuensi](references/opsi-dan-konsekuensi.md).

## Catatan distribusi

Isi skill memuat pertimbangan internal BPKP mengenai sistematika dan register naskah. Periksa ketentuan distribusi sebelum membagikannya ke luar unit.
