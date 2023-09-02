from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for number in range(players_count):
            self.players.append(Player(number=number+1))
            self.players[number].give_tiles(self.bag_tiles.take(7))

    def end_game(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False