# Инструкция по загрузке проекта в GitHub

## Шаги для загрузки проекта

### 1. Создайте репозиторий на GitHub

1. Зайдите на https://github.com
2. Нажмите кнопку "New repository"
3. Укажите название репозитория (например, `landing_new`)
4. Выберите публичный или приватный репозиторий
5. **НЕ** добавляйте README, .gitignore или лицензию (они уже есть в проекте)
6. Нажмите "Create repository"

### 2. Добавьте remote и загрузите код

После создания репозитория GitHub покажет вам команды. Выполните:

```bash
# Добавьте remote (замените YOUR_USERNAME и REPO_NAME на ваши данные)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Или если используете SSH:
git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git

# Загрузите код в GitHub
git push -u origin main
```

### 3. Альтернативный способ (если репозиторий уже создан)

Если вы уже создали репозиторий, просто выполните:

```bash
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Проверка

После выполнения команд проверьте, что код загружен:

1. Обновите страницу репозитория на GitHub
2. Убедитесь, что все файлы присутствуют
3. Проверьте, что `.gitignore` работает корректно (не должны быть видны `venv/`, `db.sqlite3`, `__pycache__/` и т.д.)

## Дальнейшая работа

Для последующих изменений используйте стандартный workflow:

```bash
# Добавить изменения
git add .

# Создать коммит
git commit -m "Описание изменений"

# Загрузить в GitHub
git push
```


