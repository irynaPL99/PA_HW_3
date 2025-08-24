from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from app_HW3 import Category, Product, Colors

#engine = create_engine('sqlite:///example.db', echo=True)
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)

with Session() as session:
    """ Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 
349.99.
    """
    # Update
    product = session.query(Product).filter_by(name="Смартфон").first()
    if product:
        # update price
        product.price = 349.99
        session.commit()
        print(f"Найден продукт и цена обновлена: {product}")
    else:
        print("Продукт с именем 'Смартфон' не найден")


    """ Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой 
категории.
    """
    # join, group by, count
    total_products_per_category = session.query(
        Category.name, func.count(Product.id)
    ).join(Product).group_by(Category.name).all()
    print("Общее количество продуктов по категориям:", total_products_per_category)

    """ Отфильтруйте и выведите только те категории, в которых более одного продукта.
    """
    # join, group by, having
    categories_with_multiple_products = session.query(
        Category.name
    ).join(Product).group_by(Category.name).having(func.count(Product.id) > 1).all()
    print("Категории с более чем одним продуктом:", categories_with_multiple_products)