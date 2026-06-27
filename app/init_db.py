from app.db.db import engine, SessionLocal
from app.db import models
from app.db.crud import create_category, create_book

def init_db():
    # Создаём таблицы (если их нет)
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Добавляем категории
    cat1 = create_category(db, "Фантастика")
    cat2 = create_category(db, "Детективы")

    # Книги для категории "Фантастика"
    create_book(db, "Дюна", "Фрэнк Герберт", 500.0, cat1.id, "https://example.com/dune")
    create_book(db, "1984", "Джордж Оруэлл", 450.0, cat1.id, "https://example.com/1984")
    create_book(db, "Властелин колец", "Дж. Р. Р. Толкин", 700.0, cat1.id, "https://example.com/lotr")

    # Книги для категории "Детективы"
    create_book(db, "Убийство в Восточном экспрессе", "Агата Кристи", 400.0, cat2.id, "https://example.com/murder")
    create_book(db, "Тень ветра", "Карлос Руис Сафон", 550.0, cat2.id, "https://example.com/shadow")

    db.close()
    print("База данных инициализирована тестовыми данными.")

if __name__ == "__main__":
    init_db()