from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey

class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    RESET = '\033[0m'


# Базовый класс для ORM
Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description={self.description})>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, category_id={self.category_id}, name='{self.name}', price={self.price}, in_stock={self.in_stock})>"


if __name__ == '__main__':
    # Создаём движок SQLite
    #engine = create_engine('sqlite:///:memory:', echo=True)
    engine = create_engine('sqlite:///example.db', echo=True)
    if engine:
        print(f"{Colors.GREEN}База данных успешно создана!{Colors.RESET}")


    Session = sessionmaker(bind=engine)
    session = Session()

    # Создаём таблицы в базе
    Base.metadata.create_all(engine)

    # Инспектор для анализа структуры БД
    inspector = inspect(engine)

    # Получаем список таблиц
    tables = inspector.get_table_names()

    if tables:
        print(f"{Colors.GREEN}Найдены таблицы:{Colors.RESET}", tables)
    else:
        print(f"{Colors.RED}Таблиц в базе данных нет.{Colors.RESET}")