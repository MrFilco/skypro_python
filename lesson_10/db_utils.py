# lesson_9/db_utils.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"

Base = declarative_base()

# Определение модели Employee для работы с таблицей employee в БД
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False, default=True)
    create_timestamp = Column(TIMESTAMP, server_default=text('now()'))
    change_timestamp = Column(TIMESTAMP, server_default=text('now()'))
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    phone = Column(String(15), nullable=False)
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer, nullable=False)

# Настройка соединения с БД
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_employee(db_session, **kwargs):
    employee = Employee(**kwargs)
    db_session.add(employee)
    db_session.commit()
    db_session.refresh(employee)
    return employee

def get_employee_by_id(db_session, employee_id):
    return db_session.query(Employee).filter(Employee.id == employee_id).first()

def delete_employee(db_session, employee_id):
    employee = db_session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db_session.delete(employee)
        db_session.commit()

def setup_db():
    """Create tables and any initial data needed for tests."""
    Base.metadata.create_all(bind=engine)

def teardown_db():
    """Clean up test data from the database."""
    with engine.connect() as connection:
        # Временно отключаем проверку внешних ключей
        connection.execute(text('SET CONSTRAINTS ALL DEFERRED'))
        # Удаляем данные из таблиц
        connection.execute(text('DELETE FROM employee'))
        # Включаем проверку внешних ключей обратно
        connection.execute(text('SET CONSTRAINTS ALL IMMEDIATE'))