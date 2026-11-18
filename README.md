# buat-policy-brief

Skill untuk menyusun dan mereviu outline serta policy brief BPKP dengan
sistematika PerLAN.

Versi saat ini: **1.3.2**. Lihat [CHANGELOG.md](CHANGELOG.md) untuk riwayat perubahan.

## Untuk pengguna baru

Mulai dari [PANDUAN.md](PANDUAN.md). Berkas itu menjelaskan cara memakai skill dari nol,
termasuk contoh perintah, contoh keluaran, dan kesalahan yang sering terjadi. README ini
hanya ringkasan isi repositori.

pull command 
git pull origin master

## Isi repositori

```
SKILL.md                        instruksi utama yang dibaca agen
PANDUAN.md                      panduan penggunaan untuk manusia
CHANGELOG.md                    riwayat versi dan catatan pengujian
README.md                       berkas ini
scripts/
  policy_brief_to_docx.py       konversi Markdown ke .docx (opsional, butuh uv)
references/
  analisis-kebijakan.md         panduan memilih metode analisis
  model-pengawasan-bpkp.md      model naskah policy brief lengkap
  penerapan.md                  contoh penerapan untuk kepala daerah dan Presiden
  pola-bahasa-id.md             daftar periksa pola bahasa yang menandai naskah mesin
  pola-contoh.md                pola narasi dari contoh policy brief
  rubrik-diklat.md              rubrik penilaian diklat, bila penugasan memerlukannya
```

## Memasang

Salin folder ini ke direktori skill Cherry Studio atau lainnya:

```
%APPDATA%\CherryStudio\Data\Skills\buat-policy-brief\
```

Cherry Studio memindai direktori itu saat mulai. Jika skill belum muncul, mulai ulang
aplikasinya. Pastikan nama folder adalah `buat-policy-brief` dan sama dengan nilai
`name:` pada frontmatter `SKILL.md`.

## Dua cara memakai

**Hanya prosa, tanpa shell.** Seluruh penyusunan naskah berjalan tanpa `uv`. Skill membaca
referensi dan menghasilkan teks Markdown atau keluaran langsung di percakapan. Ini cara
paling sederhana dan tidak memerlukan pemasangan apa pun.

**Dengan konversi .docx.** Bila lingkungan menyediakan `uv`, naskah Markdown dapat
dikonversi menjadi .docx yang bisa diedit di Word. Lihat bagian "Keluaran berkas" pada
[PANDUAN.md](PANDUAN.md).

## Memperbarui

```bash
git pull
```

Lalu salin ulang folder ke direktori skill. Bila ingin setiap `git pull` langsung
terpakai, buat tautan simbolik sekali:

```powershell
New-Item -ItemType SymbolicLink `
  -Path "$env:APPDATA\CherryStudio\Data\Skills\buat-policy-brief" `
  -Target "$env:USERPROFILE\Documents\buat-policy-brief"
```

Perlu diketahui: dengan tautan, Cherry Studio menulis langsung ke folder repositori,
sehingga setiap perubahan tampil sebagai diff yang belum di-commit. Tanpa tautan,
perubahan harus disalin manual.

## Berkontribusi

1. Ubah berkas di folder ini.
2. Naikkan `version:` pada frontmatter `SKILL.md` bila isi berubah.
3. Catat perubahan pada `CHANGELOG.md`, termasuk apa yang diuji dan bagaimana hasilnya.
4. Commit dengan pesan yang menjelaskan alasan perubahan, bukan hanya nama berkasnya.
5. Gunakan cabang terpisah dan merge request bila perubahan besar.

## Catatan distribusi

Isi skill memuat pertimbangan internal BPKP mengenai sistematika dan register naskah.
Periksa ketentuan distribusi sebelum membagikannya ke luar unit.
