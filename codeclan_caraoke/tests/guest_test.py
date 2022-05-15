import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room
from classes.bar import Bar

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Shuna", 80.00)
        self.song = Song("Graffiti", "Chvrches")
        self.room = Room(1, 5, 5.50, 0.00)
        self.bar_item = Bar("White wine", 5)

    def test_add_favourite_song(self):
        self.guest.add_favourite_song(self.song)
        self.assertEqual(1, len(self.guest.favourite_song))

    def test_get_favourite_song(self):
        self.guest.add_favourite_song(self.song)
        self.assertEqual("Graffiti", self.guest.get_favourite_song())

    def test_cheer_loudly(self):
        self.assertEqual("Whoo!", self.guest.cheer_loudly())
    
        # test that 5.50 is taken from guest's wallet when the pay_entry_fee method is run
    def test_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room)
        self.assertEqual(74.50, self.guest.wallet)
    
        # test that 5.00 is taken from guest's wallet when they purchase an item from the bar
    def test_purchase_item(self):
        self.guest.purchase_item(self.bar_item)
        self.assertEqual(75.00, self.guest.wallet)
