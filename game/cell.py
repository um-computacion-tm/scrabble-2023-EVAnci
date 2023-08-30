from game.bagtiles import Tile

class Cell:
    def __init__(self, multiplier:int, letter_multiplier:bool):
        self.multiplier = multiplier
        self.letter_multiplier = letter_multiplier
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.letter_multiplier:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
