from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route("/")
def index():
    return render_template("index.html", title="Home")


@app.route("/<player_1_choice>/<player_2_choice>")
def play_from_url(player_1_choice, player_2_choice):
    player_1 = Player("Player One", player_1_choice)
    player_2 = Player("Player Two", player_2_choice)
    winner = Game.results(player_1, player_2)

    return render_template(
        "results.html",
        title="Results",
        winner=winner,
        player_1=player_1,
        player_2=player_2,
    )


@app.route("/play")
def play_computer():
    return render_template("play.html", title="vs The Machine")


@app.route("/play", methods=["POST"])
def play_against_computer():
    name = request.form["name"]
    choice = request.form["choice"]
    player = Player(name, choice)
    computer = Game.computer_player()
    winner = Game.results(player, computer)
    return render_template(
        "results.html",
        title="Results",
        winner=winner,
        player_1=player,
        player_2=computer,
    )
