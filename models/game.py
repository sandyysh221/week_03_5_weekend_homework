import random
from models.player import Player


class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        choices = ["rock", "paper", "scissors"]
        random_choice = random.choice(self.choices)

    def results(player_1, player_2):
        if player_1.choice == player_2.choice:
            return None

        elif player_1.choice == "rock":
            if player_2.choice == "scissors":
                return player_1
            else:
                return player_2

        elif player_1.choice == "paper":
            if player_2.choice == "rock":
                return player_1
            else:
                return player_2

        elif player_1.choice == "scissors":
            if player_2.choice == "paper":
                return player_1
            else:
                return player_2

    def computer_player():
        return Player("Computer", random.choice(["rock", "paper", "scissors"]))
