class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.favourite_song = []
        self.wallet = wallet
    
    def add_favourite_song(self, song):
        self.favourite_song.append(song)
    
    def get_favourite_song(self):
        return self.favourite_song[0].title
    
    def cheer_loudly(self):
        return "Whoo!"
    
    # customer pays entry fee attached to the room
    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee

    # customer pays for item from the room's bar
    def purchase_item(self, item):
        self.wallet -= item.price
    
