class Product:
    def __init__(self, sku, name, quantity, minimum_stock):
        self.sku = sku  # Prekes kodas
        self.name = name
        self.quantity = quantity
        self.minimum_stock = minimum_stock

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:

            return False
