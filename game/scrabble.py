from game.board import Board
from game.player import Player
from game.bagtiles import BagTiles, InsufficientTiles

class InvalidWord(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for number in range(players_count):
            self.players.append(Player(number=number+1))
            self.players[number].give_tiles(self.bag_tiles.take(7))
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def play(self, word, pos, horizontal, player):
        is_valid = self.board.validate(word,pos,horizontal)
        if is_valid:
            has_letters = player.search(word)
            if has_letters:
                tiles = player.take(word)
                self.board.put_word(tiles,pos,horizontal)
                try:
                    player.fill(self.bag_tiles)
                except InsufficientTiles:
                    if len(self.bag_tiles.tiles) != 0:
                        player.give_tiles(self.bag_tiles.take(len(self.bag_tiles.tiles)))
        else:
            raise InvalidWord

    def end_game(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False