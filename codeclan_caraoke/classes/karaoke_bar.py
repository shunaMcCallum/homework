from classes.room import Room
from classes.guest import Guest

class KaraokeBar:
    def __init__(self, name, till):
        self.name = name
        self.rooms_list = []
        self.till = till
        self.capacity = 0
    
    def add_room(self, room):
        self.rooms_list.append(room)
        self.capacity += room.capacity
    
    def remove_room(self, room):
        self.rooms_list.remove(room)
    
    def add_song_to_all_rooms(self, song):
        for room in self.rooms_list:
            room.songs.append(song)
                
    def check_guest_in(self, guest, room):
        room.check_in_guest(guest)
        self.till += room.till

    def add_bar_item_to_all_rooms(self, bar_item):
        for room in self.rooms_list:
            room.bar_list.append(bar_item)
        
    # def update_bar_item_to_all_rooms(self, bar_item):
    #     for room in self.rooms_list:
    #         if bar_item in room.bar_list:
    #             bar_item.stock_level += 1
    #         else: 
    #             self.add_bar_item_to_all_rooms(bar_item)

        # FURTHER BAR METHODS TO WRITE HERE:
        # Get stock from all rooms - total stock (new property required for this???)
        # Remove stock from all rooms
        # Get value of total stock
    

    