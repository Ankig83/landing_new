"""
WSGI файл для запуска Django приложения на Beget через Passenger
"""
import os
import sys

# Добавляем путь к проекту в sys.path
# ЗАМЕНИТЕ 'yourdomain.com' на ваш домен
# ЗАМЕНИТЕ 'u1234567' на ваш username на Beget
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

# Устанавливаем переменные окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Импортируем WSGI приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

