from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from app_HW3 import Category, Product, Colors

engine = create_engine('sqlite:///example.db', echo=True)
Session = sessionmaker(bind=engine)


with Session() as session:
    # add categories
    categories = [
        Category(name="Электроника", description="Гаджеты и устройства."),
        Category(name="Книги", description="Печатные книги и электронные книги."),
        Category(name="Одежда", description="Одежда для мужчин и женщин."),
    ]
    # add products
    products = [
        Product(name="Смартфон", price=299.99, in_stock=True,
                category=categories[0]),
        Product(name="Ноутбук", price=499.99, in_stock=True,
                category=categories[0]),
        Product(name="Научно-фантастический роман", price=15.99, in_stock=True,
                category=categories[1]),
        Product(name="Джинсы", price=40.50, in_stock=False,
                category=categories[2]),
        Product(name="Футболка", price=20.00, in_stock=True,
                category=categories[2]),
    ]
    session.add_all(categories + products)
    session.commit()
    print(f"{Colors.GREEN}✅ categories and products inserted successfully!{Colors.RESET}\n")

    # Read
    for category in session.query(Category).all():
        print(f"{Colors.GREEN}Категория: {category.name}, Описание: {category.description}{Colors.RESET}")
        for product in category.products:
            print(f"Продукт: {product.name}, Цена: {product.price}, В наличии: {product.in_stock}")