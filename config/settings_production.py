"""
Настройки Django для продакшена на Beget
Импортируйте этот файл в settings.py для продакшена
"""
from .settings import *
import os

# Отключаем режим отладки в продакшене
DEBUG = False

# ALLOWED_HOSTS (через env, список доменов через запятую)
# Пример: DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
_allowed_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(",") if h.strip()] if _allowed_hosts else ALLOWED_HOSTS

# Безопасный SECRET_KEY (используйте переменную окружения в продакшене)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", SECRET_KEY)

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
def _env_bool(name: str, default: bool) -> bool:
    return os.environ.get(name, "1" if default else "0").lower() in {"1", "true", "yes", "on"}

# Включайте, если сайт обслуживается по HTTPS (иначе возможны редирект-лупы).
SECURE_SSL_REDIRECT = _env_bool("DJANGO_SECURE_SSL_REDIRECT", False)
SESSION_COOKIE_SECURE = _env_bool("DJANGO_SESSION_COOKIE_SECURE", SECURE_SSL_REDIRECT)
CSRF_COOKIE_SECURE = _env_bool("DJANGO_CSRF_COOKIE_SECURE", SECURE_SSL_REDIRECT)

# HSTS имеет смысл только при HTTPS
SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_SECURE_HSTS_SECONDS", "0"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = _env_bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", False)
SECURE_HSTS_PRELOAD = _env_bool("DJANGO_SECURE_HSTS_PRELOAD", False)

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

