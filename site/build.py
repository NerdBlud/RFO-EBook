"""Build the RFO reader from the numbered lesson PDFs."""

from html import escape
from pathlib import Path
from urllib.parse import quote
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"
OUTPUT = ROOT / "dist"
RULE = """<svg class="sq rough" viewBox="0 0 800 10" preserveAspectRatio="none" aria-hidden="true">
<path d="M2 5C120 2 220 8 340 5S580 3 798 6"/></svg>"""


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


def page(title, content, prefix="", script="", current="catalog"):
    catalog_current = ' aria-current="page"' if current == "catalog" else ""
    terms_current = ' aria-current="page"' if current == "terms" else ""
    return f"""<!doctype html>
<html lang="az">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>{escape(title)}</title>
<link rel="stylesheet" href="{prefix}style.css">
<script defer src="{prefix}reader.js"></script>
{script}
</head>
<body>
<svg width="0" height="0" class="filter-definitions" aria-hidden="true">
  <filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".03" numOctaves="3" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="3.2"/></filter>
</svg>
<a class="skip" href="#main">Məzmuna keç</a>
<header><div class="w">
  <a class="logo" href="{prefix}index.html"><svg viewBox="0 0 30 30" class="rough" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="24" height="22" rx="4"/><path d="M12 12l-3 3 3 3M18 12l3 3-3 3"/></svg>RFO E-Kitabı</a>
  <nav aria-label="Əsas menyu"><a href="{prefix}index.html#modules"{catalog_current}>Dərslər</a>
  <a href="{prefix}reuse.html"{terms_current}>İstifadə şərtləri</a>
  <button class="tg" type="button" data-theme-toggle aria-label="Qaranlıq rejim" aria-pressed="false" hidden>◐</button></nav>
</div></header>
<main class="w" id="main">{content}</main>
<footer><div class="w"><span>NerdBlud materialları əsasında hazırlanıb.</span><a href="https://github.com/NerdBlud/RFO-EBook">GitHub mənbəyi</a></div></footer>
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
    for asset in ("style.css", "search.js", "reader.js"):
        shutil.copyfile(SOURCE / asset, OUTPUT / asset)
    shutil.copytree(SOURCE / "fonts", OUTPUT / "fonts", dirs_exist_ok=True)

    def slug(number, path):
        return f"{number:02}-{numbered(path)[0]:02}"

    def lesson_link(entry, label):
        number, _, path = entry
        return f'<a href="{slug(number, path)}.html"><small>{label}</small><b>{escape(numbered(path)[1])}</b></a>'

    sections = []
    for number, title, paths in modules:
        items = "".join(
            f'<li data-lesson="m{number:02}-{numbered(path)[0]}" data-topics="{escape(descriptions.get((number, path.name), ""), quote=True)}">'
            f'<a href="lessons/{slug(number, path)}.html"><span class="i">{numbered(path)[0]}</span>'
            f'<span class="t">{escape(numbered(path)[1])}</span><span class="c rough" aria-hidden="true"></span></a></li>'
            for path in paths
        )
        sections.append(f"""<section class="mod" id="modul-{number}" data-module>
  <div><div class="no">{number:02}</div><h3>{escape(title)}</h3><small data-module-progress hidden></small></div>
  <ol>{items}</ol>
</section>{RULE}""")
    hatch = "".join(
        f'<path d="M{86 + i * 2} {100 + i * 30}L{300 - i * 2} {58 + i * 30}" stroke="var(--pencil)" stroke-width="3" opacity=".75"/>'
        for i in range(9)
    )
    index = f"""<section class="hero">
  <div>
    <h1>İnformatika olimpiadalarına <i>hazırlıq</i></h1>
    <p class="lead">Azərbaycan dilində C++ dərsləri və məşq materialları. Əsas sintaksisdən qraflara, dinamik proqramlaşdırmaya və qabaqcıl alqoritmlərə qədər.</p>
    <a class="go" href="lessons/{slug(flattened[0][0], flattened[0][2])}.html">İlk dərsə başla <span aria-hidden="true">⟶</span></a>
    <div class="prog" hidden><span data-total-progress></span><progress max="{len(flattened)}" value="0" aria-label="Tamamlanan dərslər"></progress></div>
  </div>
  <svg class="book rough" viewBox="0 0 360 420" role="img" aria-label="RFO kitabı">
    <path d="M96 400L66 52L318 26L342 360Z" fill="none" stroke="var(--ink)" stroke-width="2.4" stroke-linejoin="round"/>
    <path d="M76 392L48 60M86 398L57 56" fill="none" stroke="var(--ink)" stroke-width="1.4" opacity=".5"/>
    {hatch}
    <text x="112" y="190" font-family="Caveat,cursive" font-weight="700" font-size="98" fill="var(--ink)" transform="rotate(-6 120 190)">RFO</text>
    <text x="124" y="246" font-family="Caveat,cursive" font-weight="700" font-size="46" fill="var(--ink)" transform="rotate(-6 124 240)">E-Kitabı</text>
    <text class="note" x="236" y="330">&lt;/&gt;</text>
    <path d="M250 392C290 410 322 408 346 388" fill="none" stroke="var(--pen)" stroke-width="2" stroke-linecap="round"/>
  </svg>
</section>{RULE}
<section id="modules" aria-labelledby="modules-title">
  <div class="sec"><h2 id="modules-title">Dərs kataloqu</h2>
  <div class="search" hidden><label for="lesson-search">Mövzu və ya dərs axtar</label>
  <input id="lesson-search" type="search" placeholder="Məsələn, ikili axtarış"></div></div>
  <p id="result-status" role="status" hidden></p>
  <div class="catalog">{''.join(sections)}</div>
</section>"""
    (OUTPUT / "index.html").write_text(page("RFO E-Kitabı", index, script='<script defer src="search.js"></script>'), encoding="utf-8")

    for index, (number, module, path) in enumerate(flattened):
        name = numbered(path)[1]
        summary = descriptions.get((number, path.name))
        summary_html = f'<p class="lead">{escape(summary)}</p>' if summary else ""
        key = slug(number, path)
        pdf_name = quote(f"{key}-{path.name}")
        shutil.copyfile(path, OUTPUT / "pdf" / f"{key}-{path.name}")
        previous = lesson_link(flattened[index - 1], "Əvvəlki dərs") if index else ""
        following = lesson_link(flattened[index + 1], "Növbəti dərs") if index + 1 < len(flattened) else ""
        content = f"""<article class="lesson">
  <div class="crumb"><a href="../index.html#modul-{number}">Dərslər</a> / Modul {number:02}, {escape(module)}</div>
  <div class="lh">
  <h1>{escape(name)}</h1>
  {summary_html}
  <div class="act"><a class="go" href="../pdf/{pdf_name}">PDF-i aç</a>
  <a class="go soft" href="../pdf/{pdf_name}" download>PDF-i endir</a>
  <button class="go soft" type="button" data-complete="m{number:02}-{numbered(path)[0]}" aria-pressed="false" hidden>Dərsi tamamla</button></div>
  </div>
  <iframe class="lesson-pdf" title="{escape(name, quote=True)}" src="../pdf/{pdf_name}" loading="lazy"></iframe>
  <nav class="pn" aria-label="Dərslər arasında keçid">{previous}{following}</nav>
</article>"""
        (OUTPUT / "lessons" / f"{key}.html").write_text(page(f"{name} · RFO E-Kitabı", content, "../"), encoding="utf-8")

    reuse = f"""<article class="terms">
<h1>İstifadə şərtləri</h1>
{RULE}<section>
<h2>Dərs materialları</h2>
<p>NerdBlud-un orijinal dərs mətnlərini və diaqramlarını CC BY 4.0 şərtləri ilə paylaşa və uyğunlaşdıra bilərsiniz. Müəllifi və mənbəni göstərin, lisenziyaya keçid verin və etdiyiniz dəyişiklikləri qeyd edin.</p>
<p><a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></p>
</section>{RULE}<section>
<h2>Kod nümunələri</h2>
<p>NerdBlud-un orijinal kod nümunələrini MIT lisenziyası ilə istifadə edə bilərsiniz. Kodu yayarkən müəlliflik və lisenziya bildirişlərini saxlayın.</p>
<p><a href="LICENSE-MIT">MIT lisenziyasının tam mətni</a></p>
</section>{RULE}<section>
<h2>Üçüncü tərəf materialları</h2>
<p>Xarici yarış platformalarına aid məsələlər, sitatlar və digər materiallar öz hüquq sahiblərinin şərtlərinə tabedir.</p>
</section></article>"""
    (OUTPUT / "reuse.html").write_text(page("İstifadə şərtləri · RFO E-Kitabı", reuse, current="terms"), encoding="utf-8")
    shutil.copyfile(ROOT / "LICENSE-MIT", OUTPUT / "LICENSE-MIT")
    print(f"Built {len(flattened)} lessons in {len(modules)} modules.")


if __name__ == "__main__":
    build()
