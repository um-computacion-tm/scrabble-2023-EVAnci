from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for number in range(players_count):
            self.players.append(Player(number=number))
