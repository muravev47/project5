from db.db import engine, Base, SessionLocal
from db.crud import create_category, create_book
from db.models import Category, Book

Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()

    cat1 = create_category(db, "Программирование")
    cat2 = create_category(db, "Художественная литература")

    create_book(db, "Python для начинающих", "Основы языка", 1200.0, cat1.id)
    create_book(db, "SQLAlchemy в деталях", "Продвинутый уровень", 1500.0, cat1.id)
    create_book(db, "Мастер и Маргарита", "Классика", 800.0, cat2.id)
    create_book(db, "1984", "Антиутопия", 750.0, cat2.id)

    db.close()
    print("База данных успешно инициализирована!")

if __name__ == "__main__":
    init_db()
