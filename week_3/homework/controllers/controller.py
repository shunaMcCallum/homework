from flask import render_template, request
from app import app
from models.player import *
from models.game import *
from models.players import player1, player2


@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play')
def play_page():
    return render_template("play.html")

@app.route('/<player1_choice>/<player2_choice>')
def game(player1_choice, player2_choice):    
    player1.choice = str.lower(player1_choice)
    player2.choice = str.lower(player2_choice)

    result = (Game.full_game(player1, player2))

    return render_template('game_result.html', title='Game Result', game_type="Player vs Player Game", name_1=player1.name, player1_choice=player1.choice, name_2=player2.name, player2_choice=player2.choice, result=result)

@app.route('/play/computer')
def comp_game():
    return render_template("comp_game.html", game_type="Player vs Bongo Cat", title="Play Computer Game")

@app.route('/play/result', methods=['POST'])
def comp_result():
    name = request.form['name']
    choice = request.form['player_choice']

    player = Player(name)
    player.choice = choice

    comp_player = Game.computer_player()

    result = (Game.full_game(player, comp_player))

    return render_template('game_result.html', title='Game Result', game_type="Player vs Bongo Cat", name_1=player.name, player1_choice=player.choice, name_2=comp_player.name, player2_choice=comp_player.choice, result=result)

