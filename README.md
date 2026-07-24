# Методология Po-helper — документация

Публичная документация на методологию **Po-helper**: AI-Native Product Discovery и
Трансформация PAF. Сайт: **https://po-helper-org.github.io/docs/**

Собирается на [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Разделы

| Раздел | Что внутри |
|--------|------------|
| `docs/ai-processes/` | AI-Native фреймворк Product Discovery: 9 вех (Step 0…8) × движок Product Sprint + опер-модель и fit-точки |
| `docs/ai-transformation/` | Принципы AI-Native команды по PAF (Тихомиров С.), источники `[S1]–[S7]` |

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

- Материалы **AI-Трансформации (PAF)** (`docs/ai-transformation/`) —
  [CC BY-SA 4.0](LICENSE-CC-BY-SA), автор **Тихомиров Сергей**.
- Остальное — [MIT](LICENSE).
