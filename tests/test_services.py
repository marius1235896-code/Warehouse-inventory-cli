import unittest
from models import Product
from services import find_product_by_sku
from services import find_product_by_sku, create_product, delete_product


class TestFindProductBySku(unittest.TestCase):
    def test_find_existing_product(self):
        cardboard_boxes = Product("BOX-001",  "Cardboard boxes", 120, 30)
        packing_tape = Product("BOX-002", "Packing tape", 18, 10)

        products = [cardboard_boxes, packing_tape]
        found_product = find_product_by_sku(products, "BOX-002")

        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.name, "Packing tape")

    def test_find_missing_product(self):
        cardboard_boxes = Product("BOX-001",  "Cardboard boxes", 120, 30)
        packing_tape = Product("BOX-002", "Packing tape", 18, 10)

        products = [cardboard_boxes, packing_tape]
        found_product = find_product_by_sku(products, "BOX-999")

        self.assertIsNone(found_product)

    def test_create_product(self):
        products = []
        create_product(products, "TEST-003", "Test product", 10, 2)
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].sku, "TEST-003")

    def test_create_product_with_existing_sku(self):
        existing_product = Product("BOX-001", "Existing item", 10, 2)
        products = [existing_product]
        create_product(products, "BOX-001", "Another item", 5, 1)
        self.assertEqual(len(products), 1)

    def test_delete_product(self):
        existing_product = Product("BOX-001", "Existing item", 10, 2)
        products = [existing_product]
        delete_product(products, "BOX-001")
        self.assertEqual(len(products), 0)

    def test_try_not_existed_delete_product(self):
        existing_product = Product("BOX-001", "Existing item", 10, 2)
        products = [existing_product]
        delete_product(products, "BOX-999")
        self.assertEqual(len(products), 1)
