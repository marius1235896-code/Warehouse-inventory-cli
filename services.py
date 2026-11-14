from models import Product


def find_product_by_sku(products, sku):
    for product in products:
        if product.sku == sku:
            return product

    return None


def process_order(products, order_sku, order_quantity):

    if order_quantity > 0:
        found_product = find_product_by_sku(products, order_sku)
        if found_product != None:
            stock_removed = found_product.remove_stock(order_quantity)
            print(f"{found_product.name} - {found_product.quantity}")
            if not stock_removed:
                print("Not enough stock")
            return stock_removed
        else:
            print("Product not found")
    else:
        print("Order quantity must be greater than 0")


def create_product(products, sku, name, quantity, minimum_stock):

    if quantity < 0 or minimum_stock < 0:
        print("Can't be less than 0")
    # is not None reiskia buvo rastas
    if find_product_by_sku(products, sku) is not None:
        print("This sku already created!")
        return
    else:
        new_product = Product(sku, name, quantity, minimum_stock)
        products.append(new_product)
        print("Product successfully created")


def delete_product(products, sku):
    product_to_delete = find_product_by_sku(products, sku)
    if product_to_delete is None:
        print("Product not found")
    else:

        # is products(sarasas) pasalink rasta produkta(product_to_delete)
        products.remove(product_to_delete)
        print("Product was deleted")
