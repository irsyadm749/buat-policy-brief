#!/usr/bin/env python3
"""Konversi naskah policy brief dari Markdown ke .docx.

Ketergantungan: python-docx. Jalankan lewat uv agar tidak memasang apa pun
secara global:

    uv run --with python-docx python scripts/policy_brief_to_docx.py \
        --in naskah.md --out naskah.docx

Skrip ini OPSIONAL. Bila uv atau python-docx tidak tersedia, seluruh alur
penyusunan naskah pada SKILL.md tetap berlaku dan keluaran tetap berupa teks.

Periksa ketersediaan tanpa mengonversi:

    uv run --with python-docx python scripts/policy_brief_to_docx.py --probe

Yang didukung: heading (# sampai ####), paragraf, daftar butir, daftar
bernomor, tabel GFM, tebal (**x**), miring (*x*), dan garis --- sebagai
pemisah halaman. Yang tidak didukung: gambar, catatan kaki, sitasi otomatis.
"""

from __future__ import annotations

import argparse
import re
import sys

BULLET = re.compile(r"^\s*[-*+]\s+(.*)$")
ORDERED = re.compile(r"^\s*\d+[.)]\s+(.*)$")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
RULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")
LINK_GROUP = re.compile(r"^\[([^\]\n]+)\]\(([^)\s]+)\)$")

INLINE = re.compile(
    r"(\[[^\]\n]+\]\([^)\s]+\)"
    r"|\*\*.+?\*\*|__.+?__|\*[^*\n]+?\*|_[^_\n]+?_)"
)


def add_hyperlink(par, url, label):
    """Sisipkan hyperlink biru bergaris bawah ke paragraf."""
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    part = par.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )

    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)

    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")

    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)

    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rpr.append(underline)

    run.append(rpr)

    text = OxmlElement("w:t")
    text.text = label
    text.set(qn("xml:space"), "preserve")
    run.append(text)

    link.append(run)
    par._p.append(link)


def add_runs(par, text, stats=None):
    """Tulis teks ke paragraf, menangani **tebal**, *miring*, dan [tautan](url)."""
    for part in INLINE.split(text):
        if not part:
            continue
        m = LINK_GROUP.fullmatch(part)
        if m:
            label, url = m.group(1), m.group(2)
            try:
                add_hyperlink(par, url, label)
                if stats is not None:
                    stats["link"] = stats.get("link", 0) + 1
            except Exception:
                # URL tidak sah: tulis sebagai teks agar tidak hilang diam-diam
                par.add_run(label + " (" + url + ")")
                if stats is not None:
                    stats["link_failed"] = stats.get("link_failed", 0) + 1
        elif (part.startswith("**") and part.endswith("**")) or (
            part.startswith("__") and part.endswith("__")
        ):
            run = par.add_run(part[2:-2])
            run.bold = True
        elif (part.startswith("*") and part.endswith("*")) or (
            part.startswith("_") and part.endswith("_")
        ):
            run = par.add_run(part[1:-1])
            run.italic = True
        else:
            par.add_run(part)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def convert(md: str, out_path: str, title: str) -> dict:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt

    doc = Document()
    stats = {"heading": 0, "paragraph": 0, "bullet": 0, "ordered": 0,
             "table": 0, "table_row": 0, "page_break": 0, "unparsed_table": 0,
             "link": 0, "link_failed": 0}

    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(1.8)
    sec.left_margin = Cm(1.7)
    sec.right_margin = Cm(1.7)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    lead = footer.add_run(title + "  |  halaman ")
    lead.font.size = Pt(8)
    field_run = footer.add_run()
    field_run.font.size = Pt(8)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    field_run._r.append(begin)
    field_run._r.append(instr)
    field_run._r.append(end)

    pipe_lines = sum(1 for ln in md.splitlines() if ln.lstrip().startswith("|"))
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        if not raw.strip():
            i += 1
            continue

        m = HEADING.match(raw)
        if m:
            h = doc.add_heading(level=min(len(m.group(1)), 4))
            add_runs(h, m.group(2).strip(), stats)
            stats["heading"] += 1
            i += 1
            continue

        if RULE.match(raw):
            doc.add_page_break()
            stats["page_break"] += 1
            i += 1
            continue

        if raw.lstrip().startswith("|") and i + 1 < len(lines) and TABLE_SEP.match(lines[i + 1]):
            header = split_row(raw)
            i += 2
            body = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                body.append(split_row(lines[i]))
                i += 1
            table = doc.add_table(rows=1, cols=len(header))
            table.style = "Table Grid"
            for c, text in enumerate(header):
                cell = table.rows[0].cells[c]
                cell.text = ""
                add_runs(cell.paragraphs[0], text, stats)
                for run in cell.paragraphs[0].runs:
                    run.bold = True
            for row in body:
                cells = table.add_row().cells
                for c in range(min(len(row), len(header))):
                    cells[c].text = ""
                    add_runs(cells[c].paragraphs[0], row[c], stats)
            stats["table"] += 1
            stats["table_row"] += len(body)
            doc.add_paragraph()
            continue

        mb = BULLET.match(raw)
        if mb:
            add_runs(doc.add_paragraph(style="List Bullet"), mb.group(1).strip(), stats)
            stats["bullet"] += 1
            i += 1
            continue

        mo = ORDERED.match(raw)
        if mo:
            add_runs(doc.add_paragraph(style="List Number"), mo.group(1).strip(), stats)
            stats["ordered"] += 1
            i += 1
            continue

        buf = [raw.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if not nxt.strip():
                i += 1
                break
            if (
                HEADING.match(nxt)
                or BULLET.match(nxt)
                or ORDERED.match(nxt)
                or RULE.match(nxt)
                or nxt.lstrip().startswith("|")
            ):
                break
            buf.append(nxt.strip())
            i += 1
        par = doc.add_paragraph()
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        add_runs(par, " ".join(buf), stats)
        stats["paragraph"] += 1

    stats["unparsed_table"] = max(0, pipe_lines - stats["table_row"] - stats["table"])
    doc.save(out_path)
    return stats


def pipe_lines_present(path) -> bool:
    try:
        for ln in path.read_text(encoding="utf-8").splitlines():
            if ln.lstrip().startswith("|"):
                return True
    except OSError:
        return False
    return False


def probe() -> int:
    try:
        import docx
    except ImportError:
        print("python-docx: TIDAK TERSEDIA")
        print("Jalankan lewat uv: uv run --with python-docx python <skrip> ...")
        return 1
    version = getattr(docx, "__version__", "tidak diketahui")
    print("python-docx: " + str(version))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Markdown policy brief -> .docx")
    ap.add_argument("--in", dest="src", help="berkas Markdown masukan")
    ap.add_argument("--out", dest="out", help="berkas .docx keluaran")
    ap.add_argument("--title", default=None, help="teks footer (default: nama berkas)")
    ap.add_argument("--probe", action="store_true", help="periksa ketergantungan lalu keluar")
    args = ap.parse_args()

    if args.probe:
        return probe()

    if not args.src or not args.out:
        ap.error("--in dan --out wajib, kecuali dengan --probe")
        return 2

    if probe() != 0:
        return 2

    from pathlib import Path

    src = Path(args.src)
    if not src.is_file():
        print("berkas tidak ditemukan: " + str(src), file=sys.stderr)
        return 2

    md = src.read_text(encoding="utf-8")
    title = args.title or src.stem.replace("-", " ").replace("_", " ").title()
    stats = convert(md, args.out, title)
    print("selesai: " + args.out)
    print("  heading         : %d" % stats["heading"])
    print("  paragraf        : %d" % stats["paragraph"])
    print("  butir           : %d" % stats["bullet"])
    print("  bernomor        : %d" % stats["ordered"])
    print("  tabel           : %d (%d baris)" % (stats["table"], stats["table_row"]))
    print("  pemisah halaman : %d" % stats["page_break"])
    print("  tautan          : %d" % stats["link"])
    if stats.get("link_failed"):
        print("  PERINGATAN: %d tautan gagal dibuat dan ditulis sebagai teks." % stats["link_failed"], file=sys.stderr)
    if stats["table"] == 0 and pipe_lines_present(Path(args.src)):
        print("  PERINGATAN: berkas memuat baris berpipa tetapi tidak ada tabel yang terbentuk.", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
