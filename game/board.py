from game.cell import Cell

class Board():
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

    def calculate_word_value(self, word):
        points = 0
        for cell in word:
            points += cell.calculate_value()
        return points