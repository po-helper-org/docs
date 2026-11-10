#!/usr/bin/env python3
"""Сборка PDF-гайда для руководителей.

Markdown (guide/src/*.md, по порядку имён) → HTML (pandoc) → PDF (WeasyPrint).

    pip install weasyprint      # pandoc должен быть установлен в системе
    python3 guide/build.py      # → guide/dist/ai-agents-leaders-guide.pdf
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
OUT_PDF = DIST / "ai-agents-leaders-guide.pdf"
OUT_HTML = DIST / "guide.html"

TITLE = "ИИ-агенты в управлении"
SUBTITLE = "Практическое руководство для руководителей: от личной эффективности до трансформации департамента"
EDITION = "Редакция 1.0 · 2026"

# Слова, которых не должно быть в тексте гайда (упоминания конкретных компаний-работодателей).
FORBIDDEN = re.compile(r"\bМТС\b|\bMTS\b|мтс", re.IGNORECASE)


def md_to_html() -> str:
    files = sorted(SRC.glob("*.md"))
    if not files:
        sys.exit("нет файлов в guide/src")
    text = "\n\n".join(f.read_text(encoding="utf-8") for f in files)
    bad = FORBIDDEN.findall(text)
    if bad:
        sys.exit(f"в тексте найдены запрещённые упоминания: {sorted(set(bad))}")
    res = subprocess.run(
        ["pandoc", "-f", "markdown+smart-implicit_figures+implicit_figures", "-t", "html5",
         "--wrap=none"],
        input=text, capture_output=True, text=True, check=True,
    )
    return res.stdout


def build_toc(body: str) -> str:
    """Оглавление по h1 (части) и h2 (главы) с номерами страниц через target-counter."""
    items = []
    for m in re.finditer(r'<h([12])\s+([^>]*)>(.*?)</h\1>', body, re.S):
        level, attrs, inner = m.group(1), m.group(2), m.group(3)
        idm = re.search(r'id="([^"]+)"', attrs)
        if not idm or "notoc" in attrs:
            continue
        label = re.sub(r"<[^>]+>", "", inner).strip()
        cls = "toc-part" if level == "1" else "toc-ch"
        items.append(f'<li class="{cls}"><a href="#{idm.group(1)}">{label}</a></li>')
    return '<nav class="toc"><h1 class="toc-title notoc">Содержание</h1><ul>' + "\n".join(items) + "</ul></nav>"


def page(body: str) -> str:
    css = (ROOT / "style.css").read_text(encoding="utf-8")
    cover = f"""
<section class="cover">
  <div class="cover-top">Руководство для руководителей</div>
  <div class="cover-main">
    <div class="cover-title">{html.escape(TITLE)}</div>
    <div class="cover-sub">{html.escape(SUBTITLE)}</div>
    <ul class="cover-outcomes">
      <li><b>01</b> Как работать с ИИ-агентами: память, уверенность, делегирование, границы доверия</li>
      <li><b>02</b> Как поднять личную эффективность: пять системных замен и утренний ритуал на 45 минут</li>
      <li><b>03</b> Как поднять эффективность команды: артефакты вместо присутствия, разговор про даты, команда агентов</li>
      <li><b>04</b> Как может выглядеть трансформация департамента: уровни зрелости, роли, дорожная карта</li>
    </ul>
  </div>
  <div class="cover-bottom">
    <div>По мотивам Product Architecture Framework (PAF) и его адаптации PAF Product Ops</div>
    <div>{html.escape(EDITION)} · CC BY-SA 4.0</div>
  </div>
</section>"""
    toc = build_toc(body)
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><title>{html.escape(TITLE)}</title>
<style>{css}</style></head>
<body>{cover}{toc}<main>{body}</main></body></html>"""


def main() -> None:
    DIST.mkdir(exist_ok=True)
    body = md_to_html()
    doc = page(body)
    OUT_HTML.write_text(doc, encoding="utf-8")
    from weasyprint import HTML  # импорт здесь, чтобы ошибки pandoc видеть раньше

    HTML(string=doc, base_url=str(ROOT)).write_pdf(str(OUT_PDF))
    print(f"готово: {OUT_PDF.relative_to(ROOT.parent)}  ({OUT_PDF.stat().st_size // 1024} КБ)")


if __name__ == "__main__":
    main()
