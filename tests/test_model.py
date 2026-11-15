import unittest
from models import Product


class TestProduct(unittest.TestCase):
    def test_remove_stock_when_enough(self):
        product = Product("TEST-001", "Test item", 10, 2)
        stock_removed = product.remove_stock(3)
        self.assertTrue(stock_removed)
        self.assertEqual(product.quantity, 7)

    def test_remove_stock_when_not_enough(self):
        product = Product("TEST-001", "Test item", 10, 2)

        stock_removed = product.remove_stock(15)

        self.assertFalse(stock_removed)
        self.assertEqual(product.quantity, 10)
