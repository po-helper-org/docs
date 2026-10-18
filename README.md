# Методология Po-helper — документация

Публичная документация на методологию **Po-helper**: AI-Native Product Discovery и
Трансформация PAF. Сайт: **https://po-helper-org.github.io/docs/**

Собирается на [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Разделы

| Раздел | Что внутри |
|--------|------------|
| `docs/paf-product-ops/` | **PAF Product Ops для корпоративного PO**: теория, Playbook личной трансформации, механика в девяти шагах, приложения (лестница, гейты, сроки годности, файлы, команды) и практика в организации |
| `docs/ai-processes/` | AI-Native фреймворк Product Discovery: 9 вех (Step 0…8) × движок Product Sprint + опер-модель и fit-точки |
| `docs/ai-transformation/` | Принципы AI-Native команды по PAF (Тихомиров С.), источники `[S1]–[S7]` |
| `po-methodology/` | Исходная редакция методологии в Word |

## Локальный запуск

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
```

Сборка статики: `mkdocs build --strict`.

## Публикация

Автоматическая: push в `main` запускает GitHub Actions
(`.github/workflows/deploy.yml`), который выполняет `mkdocs gh-deploy` и публикует сайт
в ветку `gh-pages`. GitHub Pages настроен на неё.

## Лицензии

- Всё содержимое `docs/` — адаптация и производные материалы **Product Architecture Framework** (Тихомиров Сергей), распространяется под
  [CC BY-SA 4.0](LICENSE-CC-BY-SA): `docs/ai-transformation/` (автор — Тихомиров С.), `docs/ai-processes/`, `docs/paf-product-ops/`
  (адаптация — Алексей Ишманов) и быстрый старт. Адаптации **не являются официальной версией PAF**.
- Конфигурация сайта, скрипты и CI (`mkdocs.yml`, `.github/`, `requirements.txt`) — [MIT](LICENSE).
