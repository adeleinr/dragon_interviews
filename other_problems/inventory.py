import unittest
from collections import defaultdict


class Inventory:
    def __init__(self, inventory_data):
        self.price_items_map = defaultdict(list)
        self.tag_items_map = defaultdict(list)
        for item in inventory_data:
            self.price_items_map[item["price"]].append(item)
            [self.tag_items_map[tag].append(item) for tag in set(item["tags"])]

    def get_item_count_at_price(self, price) -> int:
        return len(self.price_items_map[price])

    def get_item_count_by_tag(self, tag) -> int:
        return len(self.tag_items_map[tag])

class TestInventory(unittest.TestCase):
    data = [
        {"name": "Apple", "price":50, "tags":["fruit", "organic"]},
        {"name": "Banana", "price": 70, "tags": ["fruit", "organic"]},
        {"name": "Rice", "price": 50, "tags": ["grain", "organic"]},
    ]
    inventory = Inventory(data)
    testcases_items_at_price = [
        (50, 2),
    ]
    testcases_items_by_tag = [
        ("fruit", 2),
    ]

    def test_get_item_count_at_price(self):
        for testcase in self.testcases_items_at_price:
            assert(self.inventory.get_item_count_at_price(testcase[0]) == testcase[1])

    def test_get_items_by_tah(self):
        for testcase in self.testcases_items_by_tag:
            assert(self.inventory.get_item_count_by_tag((testcase[0])) == testcase[1])


unittest.main()

