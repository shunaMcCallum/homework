import unittest

from models.player import *

class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.player = Player("New Player", "rock")

    def test_player_has_name(self):
       self.assertEqual("New Player", self.player.name)
    
    def test_player_has_choice(self):
        self.assertEqual("rock", self.player.choice)

    