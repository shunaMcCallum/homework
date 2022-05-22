from models.player import *
from random import randint

class Game():

    def play_game(choice1, choice2):
        if choice1 == "rock":
            if choice2 == "rock":
                return None
            elif choice2 == "paper":
                return "choice2"
            elif choice2 == "scissors":
                return "choice1"
            else:
                return "Invalid"     
        elif choice1 == "paper":
            if choice2 == "rock":
                return "choice1"
            elif choice2 == "paper":
                return None
            elif choice2 == "scissors":
                return "choice2"
            else:
                return "Invalid"
        elif choice1 == "scissors":
            if choice2 == "rock":
                return "choice2"
            elif choice2 == "paper":
                return "choice1"
            elif choice2 == "scissors":
                return None
            else:
                return "Invalid"
        else:
            return "Invalid"

    def full_game(player1, player2):
        result = Game.play_game(player1.choice, player2.choice)
        if result == None:
            return "Draw"
        elif result == "choice1":
            return f"{player1.name} wins by playing {player1.choice}"
        elif result == "choice2":
            return f"{player2.name} wins by playing {player2.choice}"
        elif result == "Invalid":
            return "Invalid choice, please choose between rock, paper or scissors"
            
    def computer_player():
        comp_player = Player("Bongo Cat")

        num = randint(1,3)
        if num == 1:
            comp_player.choice = "rock"
        elif num == 2:
            comp_player.choice = "paper"
        elif num == 3:
            comp_player.choice = "scissors"
        
        return comp_player