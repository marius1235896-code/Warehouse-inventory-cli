import json
from models import Product


def save_products(products):
    products_data = []
    for product in products:
        product_data = {"sku": product.sku, "name": product.name, "quantity": product.quantity,
                        # cia toks naujas sarasas-zodynas kurio reikia kad suprastu json
                        "minimum_stock": product.minimum_stock}
        products_data.append(product_data)
    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)


def load_products():
    try:
        with open("inventory.json", "r") as file:
            products_data = json.load(file)
    except FileNotFoundError:
        return []
    loaded_products = []

    for product_data in products_data:
        loaded_product = Product(
            product_data["sku"],
            product_data["name"],
            product_data["quantity"],
            product_data["minimum_stock"]
        )
        loaded_products.append(loaded_product)

    return loaded_products


def save_order_history(order_history):
    with open("order_history.json", "w") as file:
        json.dump(order_history, file, indent=4)


def load_order_history():
    try:
        with open("order_history.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
