import unittest

from models.player import *
from models.game import *

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.rock = Player("Player - Rock", "Rock")
        self.paper = Player("Player - Paper", "Paper")
        self.scissors = Player("Player - Scissors", "Scissors")


    def test_rock_beats_scissors(self):
        winner = self.game.play(self.rock, self.scissors)
        self.assertEqual(self.rock, winner)


    def test_scissors_loses_to_rock(self):
        winner = self.game.play(self.scissors, self.rock)
        self.assertEqual(self.rock, winner)


    def test_scissors_beats_paper(self):
        winner = self.game.play(self.scissors, self.paper)
        self.assertEqual(self.scissors, winner)


    def test_paper_loses_to_scissors(self):
        winner = self.game.play(self.paper, self.scissors)
        self.assertEqual(self.scissors, winner)


    def test_paper_beats_rock(self):
        winner = self.game.play(self.paper, self.rock)
        self.assertEqual(self.paper, winner)


    def test_rock_loses_to_paper(self):
        winner = self.game.play(self.rock, self.paper)
        self.assertEqual(self.paper, winner)


    def test_rock_rock_draw(self):
        winner = self.game.play(self.rock, self.rock)
        self.assertEqual(None, winner)


    def test_paper_paper_draw(self):
        winner = self.game.play(self.paper, self.paper)
        self.assertEqual(None, winner)


    def test_scissors_scissors_draw(self):
        winner = self.game.play(self.scissors, self.scissors)
        self.assertEqual(None, winner)
