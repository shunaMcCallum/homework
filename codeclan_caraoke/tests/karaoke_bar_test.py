import unittest

from classes.karaoke_bar import KaraokeBar
from classes.guest import Guest
from classes.song import Song
from classes.room import Room
from classes.bar import Bar

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.karaoke_bar = KaraokeBar("CodeClanCaraoke", 0)
        self.guest_1 = Guest("Shuna", 80.00)
        self.guest_2 = Guest("Mark", 50.00)
        self.guest_3 = Guest("Susie", 65.00)
        self.song_1 = Song("Graffiti", "Chvrches")
        self.song_2 = Song("Miss You", "Blink 182")
        self.room_1 = Room(1, 2, 5.50, 0.00)
        self.room_2 = Room(2, 5, 7.50, 0.00)
        self.bar_item_1 = Bar("White wine", 5)
        self.bar_item_2 = Bar("Red wine", 4)
        self.bar_item_3 = Bar("Fries", 4.50)
        self.bar_item_4 = Bar("Crisps", 2.50)
            
    def test_add_to_rooms_list(self):
        self.karaoke_bar.add_room(self.room_1)
        self.assertEqual(1, len(self.karaoke_bar.rooms_list))

    def test_remove_room_from_list(self):
        self.karaoke_bar.add_room(self.room_1)
        self.assertEqual(1, len(self.karaoke_bar.rooms_list))
        self.karaoke_bar.remove_room(self.room_1)
        self.assertEqual(0, len(self.karaoke_bar.rooms_list))
    
    def test_get_all_rooms_capacity(self):
        self.karaoke_bar.add_room(self.room_1)
        self.karaoke_bar.add_room(self.room_2)
        self.assertEqual(7, self.karaoke_bar.capacity)
    
    def test_add_song_to_all_rooms(self):
        self.karaoke_bar.add_room(self.room_1)
        self.karaoke_bar.add_room(self.room_2)
        self.karaoke_bar.add_song_to_all_rooms(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))
        self.assertEqual(1, len(self.room_2.songs))
    
    def test_check_guest_in(self):
        self.karaoke_bar.add_room(self.room_1)
        self.room_1.add_song(self.song_1)
        
        self.karaoke_bar.check_guest_in(self.guest_1, self.room_1)

        # check that the customer has met our entry requirements and been added to the room's guest list
        # check that the entry fee has been added to the room's till
        # check that the entry fee has been added to the karaoke bar's till
        # check the entry fee has been removed from the guest's wallet
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(5.50, self.room_1.till)
        self.assertEqual(5.50, self.karaoke_bar.till)
        self.assertEqual(74.50, self.guest_1.wallet)
    
    def test_add_bar_item_to_all_rooms(self):
        self.karaoke_bar.add_room(self.room_1)
        self.karaoke_bar.add_room(self.room_2)
        self.karaoke_bar.add_bar_item_to_all_rooms(self.bar_item_1)
        self.assertEqual(1, len(self.room_1.bar_list))
        self.assertEqual(1, len(self.room_2.bar_list))
    
    # def test_update_stock_in_all_rooms(self):
    #     self.karaoke_bar.add_room(self.room_1)
    #     self.karaoke_bar.add_room(self.room_2)
    #     self.karaoke_bar.add_bar_item_to_all_rooms(self.bar_item_1)
    #     self.karaoke_bar.update_bar_item_to_all_rooms(self.bar_item_1)
    #     self.assertEqual(2, len(self.room_1.bar_list))
    #     self.assertEqual(2, len(self.room_2.bar_list))

        # Get stock from all rooms - total stock (new property required for this???)
        # Remove stock from all rooms
        # Get value of total stock