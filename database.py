import sqlite3
from models import Product


def create_database():
    connection = sqlite3.connect("warehouse.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        sku TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        minimum_stock INTEGER NOT NULL
    )
""")

    connection.commit()
    connection.close()


def save_products_to_database(products):
    products_data = []
    for product in products:
        products_data.append(
            (product.sku, product.name, product.quantity, product.minimum_stock))

    connection = sqlite3.connect("warehouse.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products")
    cursor.executemany(
        """
    INSERT INTO products (sku, name, quantity, minimum_stock)
    VALUES (?, ?, ?, ?)
    """,
        products_data

    )
    connection.commit()
    connection.close()


def load_products_from_database():
    connection = sqlite3.connect("warehouse.db")
    cursor = connection.cursor()
    cursor.execute("SELECT sku, name, quantity, minimum_stock FROM products ")
    products_data = cursor.fetchall()
    loaded_products = []
    for product_data in products_data:
        loaded_product = Product(
            product_data[0],
            product_data[1],
            product_data[2],
            product_data[3]
        )
        loaded_products.append(loaded_product)

    connection.close()
    return loaded_products
