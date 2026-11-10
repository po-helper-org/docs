#!/usr/bin/env python3
"""Сборка гайда v2 (тестовая глава): Markdown → HTML (pandoc) → PDF (WeasyPrint).

    python3 guide/v2/build.py            # все файлы из src/ → dist/guide-v2.pdf
    python3 guide/v2/build.py 07         # только файлы, чьё имя начинается с 07
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
    doc = f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>ИИ-агенты в управлении</title><style>{css}</style></head><body>{body}</body></html>'
    out = ROOT / "dist" / (f"test-chapter-{prefix}.pdf" if prefix else "guide-v2.pdf")
    out.parent.mkdir(exist_ok=True)
    (out.with_suffix(".html")).write_text(doc, encoding="utf-8")
    from weasyprint import HTML
    HTML(string=doc, base_url=str(ROOT)).write_pdf(str(out))
    print(f"готово: {out.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
