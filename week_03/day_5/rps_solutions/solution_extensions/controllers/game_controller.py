from rps import app
from models.game import *
from models.player import *
from flask import render_template

@app.route('/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    game = Game()

    winner = game.play(player_1, player_2)

    return render_template("game.html", player_1=player_1, player_2=player_2, winner=winner)

@app.route('/rules')
def rules():
    return render_template('rules.html')
