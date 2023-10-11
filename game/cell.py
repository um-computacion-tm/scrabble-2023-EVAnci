from game.bagtiles import Tile

class Cell:
    def __init__(self, multiplier:int, letter_multiplier:bool, active=True):
        self.multiplier = multiplier
        self.letter_multiplier = letter_multiplier
        self.active = active
        self.tile = None

    def add_letter(self, tile:Tile):
        self.tile = tile

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.letter_multiplier and self.active:
            return self.tile.value * self.multiplier
        else:
            return self.tile.value

    def __repr__(self):
        if self.tile:
            return f'{self.tile}'
        else:
            return ' '
