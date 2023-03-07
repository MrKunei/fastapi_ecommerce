# fastapi_ecommerce

## Локальный запуск

Склонируйте репозиторий.

Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `source venv\scripts\activate`; Linux/Mac: `source venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.
Переименуйте `.env.example` в `.env` и заполните его.

Для локального запуска, находясь в корневой директории проекта выполните команды:
- для миграций:

```
alembic upgrade heads
```

- для запуска сервера, перейти в папку src:
```
uvicorn main:app --reload 
```
