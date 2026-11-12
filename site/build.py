"""Build the RFO reader from the numbered lesson PDFs."""

from html import escape
from pathlib import Path
from urllib.parse import quote
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"
OUTPUT = ROOT / "dist"


def numbered(path):
    match = re.match(r"^(\d+)\. (.+)$", path.stem if path.is_file() else path.name)
    if not match:
        raise ValueError(f"Missing lesson or module number: {path}")
    return int(match[1]), match[2]


def curriculum():
    modules = []
    for folder in sorted(ROOT.glob("[0-9][0-9]. *")):
        number, title = numbered(folder)
        lessons = sorted(folder.glob("*.pdf"), key=lambda path: numbered(path)[0])
        if not lessons:
            raise ValueError(f"No lessons in {folder}")
        modules.append((number, title, lessons))
    if not modules:
        raise ValueError("No numbered modules found.")
    return modules


def lesson_descriptions():
    """Use the curriculum table as the source for lesson descriptions."""
    source = (ROOT / "README.md").read_text(encoding="utf-8")
    modules = re.split(r"^### Modul (\d+):[^\n]*\n", source, flags=re.MULTILINE)
    descriptions = {}
    for number, content in zip(modules[1::2], modules[2::2]):
        for line in content.splitlines():
            match = re.match(r"^\| [^|]*`([^`]+\.pdf)`[^|]*\| (.+) \|$", line)
            if match:
                descriptions[int(number), match[1]] = match[2].replace("`", "").replace(r"\|", "|")
    return descriptions


def page(title, content, prefix="", script=""):
    return f"""<!doctype html>
<html lang="az">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{prefix}style.css">
{script}
</head>
<body>
<a class="skip" href="#main">Məzmuna keç</a>
<header class="site-header"><div class="frame header-inner">
  <a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">&lt;/&gt;</span> RFO E-Kitabı</a>
  <nav aria-label="Əsas keçidlər"><a href="{prefix}index.html#modules">Modullar</a>
  <a href="{prefix}reuse.html">İstifadə şərtləri</a></nav>
</div></header>
<main class="frame" id="main">{content}</main>
<footer class="frame"><a href="https://github.com/NerdBlud/RFO-EBook">GitHub mənbəyi</a></footer>
</body>
</html>
"""


def build():
    modules = curriculum()
    descriptions = lesson_descriptions()
    flattened = [(number, title, path) for number, title, paths in modules for path in paths]
    for number, title, path in flattened:
        if path.read_bytes()[:5] != b"%PDF-":
            raise ValueError(f"Invalid PDF header: {path}")
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "lessons").mkdir(exist_ok=True)
    (OUTPUT / "pdf").mkdir(exist_ok=True)
    for asset in ("style.css", "search.js"):
        shutil.copyfile(SOURCE / asset, OUTPUT / asset)
    shutil.copytree(SOURCE / "fonts", OUTPUT / "fonts", dirs_exist_ok=True)

    def slug(number, path):
        return f"{number:02}-{numbered(path)[0]:02}"

    def lesson_link(entry, label):
        number, _, path = entry
        return f'<a href="{slug(number, path)}.html">{label}<strong>{escape(numbered(path)[1])}</strong></a>'

    sections = []
    for number, title, paths in modules:
        items = "".join(
            f'<li data-topics="{escape(descriptions.get((number, path.name), ""), quote=True)}">'
            f'<a href="lessons/{slug(number, path)}.html">{escape(numbered(path)[1])}</a></li>'
            for path in paths
        )
        sections.append(f"""<section class="module" id="modul-{number}" data-module>
  <h3><span>{number:02}</span><span>{escape(title)}</span></h3>
  <ol>{items}</ol>
</section>""")
    index = f"""<section class="hero">
  <div class="hero-copy">
    <p class="meta">C++20 · {len(modules)} modul · {len(flattened)} dərs</p>
    <h1>İnformatika olimpiadalarına <em>hazırlıq</em></h1>
    <p>Azərbaycan dilində C++ dərsləri və məşq materialları. Əsas sintaksisdən qraflara, dinamik proqramlaşdırmaya və qabaqcıl alqoritmlərə qədər.</p>
    <a class="button" href="lessons/{slug(flattened[0][0], flattened[0][2])}.html">İlk dərsə başla <span aria-hidden="true">↗</span></a>
  </div>
  <div class="book-stage" aria-hidden="true">
    <div class="book-cover"><div class="book-type">RFO<span>E-Kitabı</span></div><div class="book-mark">&lt;/&gt;</div></div>
  </div>
</section>
<section id="modules" aria-labelledby="modules-title">
  <div class="section-heading"><h2 id="modules-title">Dərs kataloqu</h2>
  <div class="search" hidden><label for="lesson-search">Mövzu və ya dərs axtar</label>
  <input id="lesson-search" type="search" placeholder="Məsələn, ikili axtarış"></div></div>
  <p id="result-status" role="status" hidden></p>
  <div class="catalog">{''.join(sections)}</div>
</section>"""
    (OUTPUT / "index.html").write_text(page("RFO E-Kitabı", index, script='<script defer src="search.js"></script>'), encoding="utf-8")

    for index, (number, module, path) in enumerate(flattened):
        name = numbered(path)[1]
        summary = descriptions.get((number, path.name))
        summary_html = f'<p class="lesson-summary">{escape(summary)}</p>' if summary else ""
        key = slug(number, path)
        pdf_name = quote(f"{key}-{path.name}")
        shutil.copyfile(path, OUTPUT / "pdf" / f"{key}-{path.name}")
        previous = lesson_link(flattened[index - 1], "Əvvəlki dərs") if index else ""
        following = lesson_link(flattened[index + 1], "Növbəti dərs") if index + 1 < len(flattened) else ""
        content = f"""<article class="lesson">
  <a class="back" href="../index.html#modul-{number}">Modul {number:02} · {escape(module)}</a>
  <h1>{escape(name)}</h1>
  {summary_html}
  <div class="actions"><a class="button" href="../pdf/{pdf_name}">PDF-i aç</a>
  <a href="../pdf/{pdf_name}" download>PDF-i endir</a></div>
  <iframe title="{escape(name, quote=True)}" src="../pdf/{pdf_name}" loading="lazy"></iframe>
  <nav class="lesson-nav" aria-label="Dərslər arasında keçid">{previous}{following}</nav>
</article>"""
        (OUTPUT / "lessons" / f"{key}.html").write_text(page(f"{name} · RFO E-Kitabı", content, "../"), encoding="utf-8")

    reuse = """<article class="reuse">
<h1>İstifadə şərtləri</h1>
<h2>Dərs materialları</h2>
<p>NerdBlud-un orijinal dərs mətnlərini və diaqramlarını CC BY 4.0 şərtləri ilə paylaşa və uyğunlaşdıra bilərsiniz. Müəllifi və mənbəni göstərin, lisenziyaya keçid verin və etdiyiniz dəyişiklikləri qeyd edin.</p>
<p><a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></p>
<h2>Kod nümunələri</h2>
<p>NerdBlud-un orijinal kod nümunələrini MIT lisenziyası ilə istifadə edə bilərsiniz. Kodu yayarkən müəlliflik və lisenziya bildirişlərini saxlayın.</p>
<p><a href="LICENSE-MIT">MIT lisenziyasının tam mətni</a></p>
<h2>Üçüncü tərəf materialları</h2>
<p>Xarici yarış platformalarına aid məsələlər, sitatlar və digər materiallar öz hüquq sahiblərinin şərtlərinə tabedir.</p>
</article>"""
    (OUTPUT / "reuse.html").write_text(page("İstifadə şərtləri · RFO E-Kitabı", reuse), encoding="utf-8")
    shutil.copyfile(ROOT / "LICENSE-MIT", OUTPUT / "LICENSE-MIT")
    print(f"Built {len(flattened)} lessons in {len(modules)} modules.")


if __name__ == "__main__":
    build()
