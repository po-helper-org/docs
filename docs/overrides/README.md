# overrides/ — точка расширения темы

Каталог `custom_dir` темы Material.

- `main.html` — если в front matter страницы есть `robots`, выводит `<meta name="robots">`. Так закрыта от поисковиков страница книги `ai-agenty-v-upravlenii/`.
- `sitemap.xml` — карта сайта без страниц с `robots` в front matter.

Сюда же позже подключается виджет AI-чата по документации: скрипт добавляется в блок `extrahead` в `main.html`.
