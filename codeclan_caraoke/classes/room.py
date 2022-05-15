from classes.guest import Guest

class Room:
    def __init__(self, number, capacity, entry_fee, till):
        self.number = number
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []
        self.till = till
        self.bar_list = []

    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        self.songs.remove(song)

        # method to be used in case guests request full song list
    def get_list_of_songs(self):
        song_list = []
        for song in self.songs:
            song_list.append(song.title)
        return song_list
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)

        # method to be used in main check_in method to check there is enough space for the guest
    def check_room_capacity(self, guest_list):
        if self.capacity > len(guest_list):
            return True
        return False
    
        # method to be used in main check_in method to check guest has enough money for entry fee
    def check_guest_has_enough_money(self, guest):
        if guest.wallet >= self.entry_fee:
            return True
        return False
    
        # method to be used in main check_in method to collect money from guest
    def collect_fee(self):
        self.till =+ self.entry_fee

        # MAIN CHECK_IN METHOD
    def check_in_guest(self, guest):
        self.add_guest(guest)

        # check room has enough space for guest and guest has enough money
        if self.check_room_capacity(self.guests) == False:
            self.remove_guest(guest)
            return "Sorry the room is full!"
        
        if self.check_guest_has_enough_money(guest) == False:
            self.remove_guest(guest)
            return "Sorry you don't have enough money - no Caraoke for you!"

        # if the above requirements are met, it's time to party...
        self.collect_fee()
        guest.pay_entry_fee(self)

    def check_out_guest(self, guest):
        self.remove_guest(guest)

        # method to be run if guest requests favourite song, which if successful causes them to cheer_loudly
    def check_for_guests_favourite_song(self, guest):
        for song in self.songs:
            if song.title == guest.favourite_song[0]:
                return guest.cheer_loudly()
    
        # BAR METHODS:
    def add_item_to_bar(self, bar_item):
        self.bar_list.append(bar_item)
    
    def get_bar_item_by_name(self, item_name):
        for item in self.bar_list:
            if item_name == item.name:
                return item.name

    def get_bar_item_price(self, item_name):
        for item in self.bar_list:
            if item_name == item.name:
                return item.price
    
    def get_bar_item_stock_level(self, item_name):
        for item in self.bar_list:
            if item_name == item.name:
                return item.stock_level
    
    def update_bar_stock(self, bar_item):
        if bar_item in self.bar_list:
            bar_item.stock_level += 1
        else:
            self.add_item_to_bar(bar_item)
    
    def remove_item_from_stock(self, bar_item):
        if bar_item in self.bar_list:
            bar_item.stock_level -= 1
        else:
            return "Item not in stock"

    def get_total_stock(self):
        for item in self.bar_list:
            return f"{item.name}: {item.stock_level}"

        # MAIN METHOD FOR SELLING BAR ITEMS TO GUESTS
    def sell_bar_item(self, guest, item):
        # check first of all if customer is in the room - won't sell to customers not checked into room!
        if guest in self.guests:
                if self.remove_item_from_stock(item) == "Item not in stock":
                    return "Item not in stock"
                self.till += item.price
                guest.purchase_item(item)
        return "Customer not in room, cannot sell item"



