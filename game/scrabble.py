from game.board import Board, NotInternetConnection
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

    def player_points(self):
        result = ''
        for player in self.players:
            result += f'El jugador {player.number}: ({player.name}) tiene {player.points} puntos\n'
        return result

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def play(self, word, pos, horizontal):
        player = self.current_player
        try:
            is_valid = self.board.validate(word,pos,horizontal)
        except NotInternetConnection:
            is_valid = False
        if is_valid:
            no_intersections_word = self.board.get_word_without_intersections(word,pos,horizontal)
            player.points += 50 if len(no_intersections_word) == 7 else 0
            has_letters = player.search(no_intersections_word)
            if has_letters:
                tiles = player.take(no_intersections_word)
                player.points += self.board.calculate_word_value(word,pos,horizontal)
                self.board.put_word(tiles,pos,horizontal)
                try:
                    player.fill(self.bag_tiles)
                except InsufficientTiles:
                    if len(self.bag_tiles.tiles) != 0:
                        player.give_tiles(self.bag_tiles.take(len(self.bag_tiles.tiles)))
        else:
            raise InvalidWord

    def winners(self):
        winners = self.players.copy()
        for _ in range(len(winners)-1):
            for i in range(len(winners)-1):
                player = winners[i]
                next_player = winners[i+1]
                if player.points < next_player.points:
                    actual = player
                    winners[i] = next_player
                    winners[i+1] = actual
        return winners

    def end_game(self):
        end = False
        if self.current_player.giveup:
            end = True
        elif len(self.bag_tiles.tiles) == 0 and len(self.current_player.lectern) == 0:
            end = True
        elif self.current_player.times_pass == 2:
            end = True
        if end:
            for player in self.players:
                points = 0
                for tile in player.lectern:
                    points += tile.value
                player.points -= points 
                self.current_player.points += points if len(self.current_player.lectern) == 0 else 0
        return end