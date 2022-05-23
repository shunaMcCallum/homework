import random
from models.player import Player

class Game():

    def __init__(self):
        self.win_lookup = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

    def play(self, player_1, player_2):

        winner = None

        if self.win_lookup[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.win_lookup[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2

        return winner


    def generate_computer_player(self):
        all_moves = list(self.win_lookup.keys())
        computer_hand = random.choice(all_moves)
        computer = Player("Computer", computer_hand)
        return computer
