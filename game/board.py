from game.cell import Cell

class Board():
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]

    def calculate_word_value(self, word):
        points = 0
        word_multiplier = 1
        for cell in word:
            if not(cell.letter_multiplier) and cell.active:
                word_multiplier *= cell.multiplier
            points += cell.calculate_value()
            cell.active = False
        points = points * word_multiplier
        return points

    def validate_word_inside_board(self, word, location, horizontal):
        if horizontal:
            if len(word) <= len(self.grid)-location[0]:
                return True
            else:
                return False
        else:
            if len(word) <= len(self.grid)-location[1]:
                return True
            else:
                return False
    
    def put_word(self,word,location,horizontal):
        if horizontal:
            for i in range(len(word)):
                self.grid[location[0]][location[1]+i].tile = word[i]
        else:
            for i in range(len(word)):
                self.grid[location[0]+i][location[1]].tile = word[i]

    def view(self):
        view = ('                  TABLERO\n\n')
        view += (' '*8)
        for i in 'ABCDEFGHIJKLMNL':
            view += (f'{i} ')
        view += '\n'
        for row in range(len(self.grid)):
            # if the number is higher than 2 digits, then
            # you need to erase an space for correct formatting
            if row+1 < 10:
                view += (f'  {row+1}  |  ')
            else:
                view += (f' {row+1}  |  ')
            for column in range(len(self.grid[row])):
                try:
                    view += (f'{self.grid[row][column].tile.letter} ')
                except:
                    view += ('_ ')
            view += '\n'
        view += '\n'
        return view