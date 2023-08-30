from game.bagtiles import Tile

class Cell:
    def __init__(self, multiplier:int, letter_multiplier:bool, active=True):
        self.multiplier = multiplier
        self.letter_multiplier = letter_multiplier
        self.active = active
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.letter_multiplier and self.active:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
