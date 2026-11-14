from datetime import datetime
from storage import save_products, load_products, save_order_history, load_order_history
from services import find_product_by_sku, process_order, create_product, delete_product


def show_inventory(products):
    for product in products:
        print(f"\n{product.name} - {product.quantity}")
        if product.quantity <= product.minimum_stock:
            print("LOW STOCK!")


def show_order_history(order_history):
    for order_record in order_history:
        print(
            f"{order_record['sku']} - {order_record['quantity']} vnt | {order_record['created_at']}")


def show_menu():
    print("\n1 - Show inventory")
    print("2 - Search product")
    print("3 - Process order")
    print("4 - Create product")
    print("5 - Delete product")
    print("6 - Show order history")
    print("7 - Exit")


products = load_products()
order_history = load_order_history()


choice = ""

while choice != "7":

    show_menu()

    choice = input("Choose an option :")

    if choice == "1":
        show_inventory(products)

    elif choice == "2":
        search_sku = input("Enter SKU: ")
        found_product = find_product_by_sku(
            products, search_sku)  # Priskyrimas kintamajam
        if found_product is not None:
            print(f"\n{found_product.name} - {found_product.quantity}")
        else:
            print("Product not found")

    elif choice == "3":
        order_sku = input("Enter product SKU to order: ")
        while True:  # galima naudoti be kintamojo ir butinai reikia nutraukti paciam su break
            try:
                order_quantity = int(input("Enter quantity to order: "))
                order_success = process_order(
                    products, order_sku, order_quantity)
                if order_success:
                    order_record = {"sku": order_sku,
                                    "quantity": order_quantity,
                                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    order_history.append(order_record)
                    print("Order completed successfully")
                    save_order_history(order_history)
                else:
                    print("Order was rejected")
                break
            except ValueError:
                print("Quantity must be a whole number")
        save_products(products)

    elif choice == "4":
        new_sku = input("Enter new product SKU: ")
        new_name = input("Enter new prodcut name: ")
        while True:
            try:
                new_quantity = int(input("Enter product quantity: "))
                new_minimum_stock = int(input("Enter product minimum stock: "))
                break
            except ValueError:
                print("Quantity and minimu stock must be a whole number")

        create_product(products, new_sku, new_name,
                       new_quantity, new_minimum_stock)
        save_products(products)
    elif choice == "5":
        sku_to_delete = input("Enter product SKU: ")

        delete_product(products, sku_to_delete)
        save_products(products)
    elif choice == "6":
        show_order_history(order_history)
    elif choice == "7":
        print("Exit")

    else:
        print("Wrong choice!")

save_products(products)
