from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL

# Подключение к SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Определение таблицы
class Record(Base):
    __tablename__ = "records"
    id = Column(String, primary_key=True, index=True)
    data = Column(String)

# Создание таблицы, если её нет
Base.metadata.create_all(bind=engine)

# Функция для сохранения записи
def save_to_db(record_id, data):
    """Сохраняет данные в SQLite с обработкой ошибок"""
    session = SessionLocal()
    try:
        record = Record(id=record_id, data=data)
        session.add(record)
        session.commit()
    except Exception as e:
        session.rollback()  # Откатываем транзакцию при ошибке
        print(f"❌ Ошибка при сохранении в базу: {e}")
    finally:
        session.close()  # Закрываем соединение в любом случае

# Функция для получения записи
def get_record(record_id):
    """Получает данные из SQLite"""
    session = SessionLocal()
    try:
        record = session.query(Record).filter_by(id=record_id).first()
        return {"id": record.id, "data": record.data} if record else {}
    except Exception as e:
        print(f"❌ Ошибка при получении данных: {e}")
        return {}
    finally:
        session.close()