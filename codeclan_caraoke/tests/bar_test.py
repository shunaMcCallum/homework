import unittest

from classes.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar_item = Bar("White wine", 5)
            
    def test_bar_item_has_name(self):
        self.assertEqual("White wine", self.bar_item.name)

    def test_bar_item_has_price(self):
        self.assertEqual(5, self.bar_item.price)