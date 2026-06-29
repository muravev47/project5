# Book API

RESTful API для управления книгами и категориями.

## Запуск

1. Убедитесь, что PostgreSQL запущен и база `octagon_db` создана.
2. Активируйте виртуальное окружение: `source venv/bin/activate`
3. Установите зависимости: `pip install -r requirements.txt`
4. Запустите сервер: `uvicorn app.main:app --reload`
5. Откройте документацию: `http://localhost:8000/docs`

## Эндпоинты

- `/health` – проверка статуса
- `/categories/` – CRUD для категорий
- `/books/` – CRUD для книг, с фильтрацией по `category_id`