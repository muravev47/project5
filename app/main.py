# print("Hello, World! <3")

from fastapi import FastAPI
from app.api import categories, books
from app.db.db import engine
from app.db import models

# Создаём таблицы, если их ещё нет (при старте)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book API", version="1.0")

# Подключаем роутеры
app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}