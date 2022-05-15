import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room
from classes.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Shuna", 80.00)
        self.guest_2 = Guest("Mark", 50.00)
        self.guest_3 = Guest("Susie", 65.00)
        self.song_1 = Song("Graffiti", "Chvrches")
        self.song_2 = Song("Miss You", "Blink 182")
        self.room = Room(1, 2, 5.50, 0.00)
        self.bar_item_1 = Bar("White wine", 5)
        self.bar_item_2 = Bar("Red wine", 4)
        self.bar_item_3 = Bar("Fries", 4.50)
        self.bar_item_4 = Bar("Crisps", 2.50)

    def test_add_song(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, len(self.room.songs))

    def test_remove_song(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.remove_song(self.song_2)
        self.assertEqual(1, len(self.room.songs))

    def test_get_list_of_songs(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.assertEqual(['Graffiti', 'Miss You'], self.room.get_list_of_songs())

    def test_add_guest(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guests))

    def test_remove_guest(self):
        self.room.add_guest(self.guest_1)
        self.room.remove_guest(self.guest_1)
        self.assertEqual(0, len(self.room.guests))

        # check guests are able to check into rooms - this will be used within the main check_in method
    def test_check_room_capacity(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(True, self.room.check_room_capacity(self.room.guests))
    
        # check room's entry fee is added to its till when a guest checks in - this will be used within the main check_in method
    def test_collect_fee(self):
        self.room.collect_fee()
        self.assertEqual(5.50, self.room.till)
    
        # check guest has enough money to check into room - this will be used within the main check_in method
    def test_check_guest_has_enough_money(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(True, self.room.check_guest_has_enough_money(self.guest_1))

        # chec the above method works when guest does not have enough money
    def test_check_guest_not_enough_money(self):
        self.guest_1 = Guest("Shuna", 4.00)
        self.room.add_guest(self.guest_1)
        self.assertEqual(False, self.room.check_guest_has_enough_money(self.guest_1))

        # check guest can successfully check into room
    def test_check_in_guest_successful(self):
        self.room.add_song(self.song_1)

        self.room.check_in_guest(self.guest_1)

        # check that the customer has been added to the room's guest list
        # check that the entry fee has been added to the room's till
        # check the entry fee has been removed from the guest's wallet
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(5.50, self.room.till)
        self.assertEqual(74.50, self.guest_1.wallet)

        # check the correct output is given when room is full and guest tries to check in
    def test_check_in_guest_room_full(self):
        self.room.add_song(self.song_1)
        self.room.add_guest(self.guest_1)
        self.room.add_guest(self.guest_2)

        self.assertEqual("Sorry the room is full!", self.room.check_in_guest(self.guest_3))

        # check that the entry fee has NOT been added to the room's till
        # check that the number of guests inside the room has NOT increased
        # check that the entry fee has NOT been removed from the guest's wallet
        self.assertEqual(0, self.room.till)
        self.assertEqual(2, len(self.room.guests))
        self.assertEqual(65.00, self.guest_3.wallet)

        # check the correct output is given when guest tries to purchase bar item but does not have enough money
    def test_check_in_guest_not_enough_money(self):
        self.room.add_song(self.song_1)
        # resetting guest_1's wallet so they don't have enough money!
        self.guest_1 = Guest("Shuna", 3.00)

        self.assertEqual("Sorry you don't have enough money - no Caraoke for you!", self.room.check_in_guest(self.guest_1))

        # check that the entry fee has NOT been added to the room's till
        # check that the number of guests inside the room has NOT increased
        # check that the entry fee has NOT been removed from the guest's wallet
        self.assertEqual(0, self.room.till)
        self.assertEqual(0, len(self.room.guests))
        self.assertEqual(3.00, self.guest_1.wallet)

    def test_check_out_one_guest(self):
        self.room.add_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, len(self.room.guests))

        # check the room can find guest's favourite song and guest can respond with cheer_loudly method
    def test_check_for_guests_favourite_song(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.guest_1.add_favourite_song("Miss You")
        self.assertEqual("Whoo!", self.room.check_for_guests_favourite_song(self.guest_1))
    
    def test_add_item_to_bar(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.assertEqual(1, len(self.room.bar_list))
    
        # check guests can request bar items by name
    def test_get_bar_item_by_name(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.assertEqual("White wine", self.room.get_bar_item_by_name("White wine"))
    
        # check guests can check price of bar items by price
    def test_get_bar_item_price(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.assertEqual(5, self.room.get_bar_item_price("White wine"))
    
    def test_update_bar_stock(self):
        self.room.update_bar_stock(self.bar_item_1)
        self.room.update_bar_stock(self.bar_item_1)
        self.room.update_bar_stock(self.bar_item_2)
        self.assertEqual(2, self.room.get_bar_item_stock_level("White wine"))
        self.assertEqual(1, self.room.get_bar_item_stock_level("Red wine"))
    
        # check the karaoke bar can check stock levels of particular bar items
    def test_get_bar_item_stock_level(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.room.update_bar_stock(self.bar_item_1)
        self.assertEqual(2, self.room.get_bar_item_stock_level("White wine"))
    
        # check the karaoke bar can access stock levels of all drinks together
    def test_get_total_stock(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.room.update_bar_stock(self.bar_item_1)
        self.assertEqual("White wine: 2", self.room.get_total_stock())

        # test bar items can be sold successfully 
    def test_sell_bar_item_successful(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.room.update_bar_stock(self.bar_item_1)
        self.room.add_guest(self.guest_1)

        self.room.sell_bar_item(self.guest_1, self.bar_item_1)

        # check room's till has increased by drink price
        # check bar's stock level has decreased by 1
        # check customer's wallet has decreased by drink price
        self.assertEqual(5, self.room.till)
        self.assertEqual(1, self.room.get_bar_item_stock_level("White wine"))
        self.assertEqual(75.00, self.guest_1.wallet)
    
        # check correct output is given when customer tries to purchase bar item but they are not checked into the room
    def test_sell_bar_item_customer_not_in_room(self):
        self.room.add_item_to_bar(self.bar_item_1)
        self.assertEqual("Customer not in room, cannot sell item", self.room.sell_bar_item(self.guest_1, self.bar_item_1))

        # check correct output is given when customer tries to purchase bar item but the item is not in stock
    def test_sell_bar_item_not_in_stock(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual("Item not in stock", self.room.sell_bar_item(self.guest_1, self.bar_item_1))
