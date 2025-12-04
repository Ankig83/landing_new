# Лендинг проект - Кондиционирование

Проект для создания лендинга на Django по фреймам из Figma.

## Описание

Многостраничный лендинг для услуг по установке и обслуживанию сплит-систем кондиционирования. Проект состоит из 5 фреймов с различным контентом и стилями.

## Установка

```bash
# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt
```

## Запуск

```bash
# Выполнение миграций
python manage.py migrate

# Сбор статических файлов
python manage.py collectstatic

# Запуск сервера разработки
python manage.py runserver
```

## Структура проекта

- `pages/` - приложение для страниц лендинга
- `templates/pages/` - шаблоны HTML
- `static/` - статические файлы (CSS, JS, изображения)
- `media/` - загружаемые файлы
- `config/` - настройки Django проекта

## Развертывание на Beget

Подробные инструкции по развертыванию на хостинге Beget находятся в файле `BEGET_DEPLOY.md`.

## Технологии

- Django 4.2+
- HTML5/CSS3
- JavaScript
- Bootstrap (опционально)

## Автор

ankig

