#!/usr/bin/env python3
"""Сборка книги «ИИ-агенты в управлении»: Markdown → HTML (pandoc) → PDF (WeasyPrint).

    python3 guide/v2/build.py            # вся книга → dist/ai-agents-v-upravlenii.pdf
    python3 guide/v2/build.py p1         # только часть I: файлы, чьё имя начинается с p1
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FORBIDDEN = re.compile(r"\bМТС\b|\bMTS\b", re.IGNORECASE)


SHORT = r"а|и|в|во|с|со|к|ко|о|об|у|не|ни|по|на|за|из|от|до|для|без|при|про|над|под|что|как|это|но|же|ли"


def typograph(text: str) -> str:
    """Неразрывный пробел после коротких слов вне HTML-тегов и строк кода."""
    out = []
    for line in text.split("\n"):
        if line.lstrip().startswith(("<", "```", "|")) and not line.lstrip().startswith("<p"):
            out.append(line)
            continue
        out.append(re.sub(rf"(?<![\w-])({SHORT}) (?=[\wА-Яа-яЁё«(])", "\\1\u00a0", line, flags=re.IGNORECASE))
    return "\n".join(out)


TITLE = "ИИ-агенты в управлении"
SUBTITLE = "Практическое пособие для руководителей: от личной эффективности до трансформации департамента"
AUTHOR = "По материалам Product Architecture Framework (С. Тихомиров) и PAF Product Ops; CC BY-SA 4.0"
BOOK = "ai-agents-v-upravlenii.pdf"
EDITION = "Издание 1.0, ноябрь 2026"
COMPILER = ""  # имя составителя или издателя для выходных данных; пусто — строка не печатается


def cover() -> str:
    bars = "".join(f'<div style="height:{(n - 1) / 8 * 100:.1f}%"><span>{n}</span></div>' for n in range(2, 10))
    return f"""<section class="cover">
<div class="cover-top">Практическое пособие для руководителей</div>
<div class="cover-title">ИИ-агенты<br>в управлении</div>
<div class="cover-sub">От личной эффективности до трансформации департамента</div>
<div class="cover-ladder">{bars}</div>
<div class="cover-ladder-caption">Лестница доказательств: уверенность в обещании от 2 до 9</div>
<div class="cover-bottom"><span>По материалам Product Architecture Framework и PAF Product Ops</span><span>2026 · CC BY-SA 4.0</span></div>
</section>"""


def imprint() -> str:
    who = f"<p>© {COMPILER}, 2026, в части нового текста. Составитель: {COMPILER}.</p>" if COMPILER else ""
    return f"""<section class="imprint">
<p class="imprint-title">{TITLE}. Практическое пособие для руководителей</p>
<p>{EDITION}.</p>{who}
<p>Книга — производное произведение от Product Architecture Framework (автор — Сергей Тихомиров, productframework.ru) и адаптации PAF Product Ops для корпоративного PO (автор адаптации — Алексей Ишманов, po-helper-org.github.io/docs). Книга не является официальной версией PAF, авторы исходных материалов в её подготовке не участвовали.</p>
<p>Текст распространяется на условиях лицензии Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0), полный текст — creativecommons.org/licenses/by-sa/4.0/legalcode.ru. Книгу можно копировать, распространять и переделывать, в том числе в коммерческих целях, при указании авторства, ссылки на лицензию и распространении производных материалов на тех же условиях. Изменения относительно исходных материалов перечислены в приложении G.</p>
<p>Материал предоставляется «как есть», без каких-либо гарантий. Компании, люди, системы, даты и числа сквозного примера вымышлены и служат иллюстрацией. Ориентиры сроков, долей и порогов взяты из практики и требуют проверки на данных своей организации. Инструменты и их возможности меняются быстро, поэтому перед подключением агента к рабочим системам нужно проверить требования к безопасности и обработке данных, действующие в компании. Книга не заменяет юридическую консультацию. Названия продуктов и компаний принадлежат их правообладателям.</p>
<p>Шрифт Onest — SIL Open Font License 1.1.</p>
</section>"""


def toc(body: str) -> str:
    """Оглавление: части и приложения жирным, главы с подписью из строки над заголовком."""
    items = []
    pat = re.compile(r'(?:<div class="kicker">\s*<p>(?P<k>[^<]*)</p>\s*</div>\s*)?<h1[^>]*?\bid="(?P<id>[^"]+)"[^>]*>(?P<t>.*?)</h1>', re.S)
    for m in pat.finditer(body):
        hid, title = m.group("id"), re.sub(r"<[^>]+>", "", m.group("t")).replace("\n", " ").strip()
        if hid.startswith("part") or hid == "appendix":
            pm = re.search(r'<span class="partnum">([^<]*)</span>\s*</p>\s*<h1[^>]*?id="' + re.escape(hid), body, re.S)
            label = pm.group(1) if pm else ""
            items.append(f'<li class="toc-part"><a href="#{hid}">{label}. {title}</a></li>')
        else:
            items.append(f'<li class="toc-ch"><a href="#{hid}"><span class="lbl">{m.group("k") or ""}</span>{title}</a></li>')
    return '<section class="toc"><h1 id="toc">Содержание</h1><ul>' + "".join(items) + "</ul></section>"


def main() -> None:
    prefix = sys.argv[1] if len(sys.argv) > 1 else ""
    files = sorted(f for f in (ROOT / "src").glob("*.md") if f.name.startswith(prefix))
    if not files:
        sys.exit("нет исходников")
    text = "\n\n".join(f.read_text(encoding="utf-8") for f in files)
    text = typograph(text)
    if FORBIDDEN.search(text):
        sys.exit("в тексте есть запрещённое упоминание компании")
    body = subprocess.run(["pandoc", "-f", "markdown+smart", "-t", "html5", "--wrap=none"],
                          input=text, capture_output=True, text=True, check=True).stdout
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    front = "" if prefix else cover() + imprint() + toc(body)
    doc = (f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>{TITLE}</title>'
           f'<meta name="author" content="{AUTHOR}"><meta name="description" content="{SUBTITLE}">'
           f'<style>{css}</style></head><body>{front}{body}</body></html>')
    out = ROOT / "dist" / (f"{prefix}.pdf" if prefix else BOOK)
    out.parent.mkdir(exist_ok=True)
    (out.with_suffix(".html")).write_text(doc, encoding="utf-8")
    from weasyprint import HTML
    HTML(string=doc, base_url=str(ROOT)).write_pdf(str(out))
    print(f"готово: {out.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
