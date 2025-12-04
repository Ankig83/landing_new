#!/bin/bash
# Скрипт для подготовки проекта к деплою на Beget

echo "Подготовка проекта к деплою на Beget..."

# Активация виртуального окружения (если используется)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Установка зависимостей
echo "Установка зависимостей..."
pip install -r requirements.txt

# Сбор статических файлов
echo "Сбор статических файлов..."
python manage.py collectstatic --noinput

# Выполнение миграций
echo "Выполнение миграций..."
python manage.py migrate --noinput

echo "Готово! Проект подготовлен к деплою."
echo "Не забудьте:"
echo "1. Обновить пути в .htaccess (username и домен)"
echo "2. Обновить ALLOWED_HOSTS в settings.py"
echo "3. Установить DEBUG = False для продакшена"

