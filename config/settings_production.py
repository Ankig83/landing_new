"""
Настройки Django для продакшена на Beget
Импортируйте этот файл в settings.py для продакшена
"""
from .settings import *
import os

# Отключаем режим отладки в продакшене
DEBUG = False

# Добавьте ваш домен в ALLOWED_HOSTS
# Пример: ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Безопасный SECRET_KEY (используйте переменную окружения в продакшене)
# SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# Настройки базы данных для продакшена (если используете MySQL/PostgreSQL на Beget)
# Раскомментируйте и настройте при необходимости:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ.get('DB_NAME', ''),
#         'USER': os.environ.get('DB_USER', ''),
#         'PASSWORD': os.environ.get('DB_PASSWORD', ''),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '3306'),
#     }
# }

# Настройки статических файлов для продакшена
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Настройки медиа файлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Безопасность
SECURE_SSL_REDIRECT = False  # Установите True если используете SSL
SESSION_COOKIE_SECURE = False  # Установите True если используете SSL
CSRF_COOKIE_SECURE = False  # Установите True если используете SSL

# Логирование (опционально)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_errors.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

