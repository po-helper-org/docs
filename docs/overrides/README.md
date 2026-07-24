# overrides/ — точка расширения темы

Каталог `custom_dir` темы Material. Сейчас пуст (каркас).

Сюда позже подключается виджет AI-чата по документации. Типовой путь:
создать `main.html`, расширяющий базовый шаблон, и добавить `<script>` виджета
(Inkeep / DocsGPT / Kapa) в блок `extrahead` или `footer`:

    {% extends "base.html" %}
    {% block extrahead %}
      {{ super() }}
      <!-- сюда скрипт AI-чата -->
    {% endblock %}
