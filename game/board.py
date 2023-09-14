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

    def validate(self, word, pos, horizontal):
        h_space = len(word) <= len(self.grid)-pos[0]
        v_space = len(word) <= len(self.grid)-pos[1]
        is_valid = 0
        if (horizontal and h_space):
            for i in range(len(word)):
                cell = self.grid[pos[0]-1][pos[1]-1+i].tile
                if cell is None or cell.letter == word[i]:
                    is_valid += 1
        elif ((not horizontal) and v_space):
            for i in range(len(word)):
                cell = self.grid[pos[0]-1+i][pos[1]-1].tile
                if cell is None or cell.letter == word[i]:
                    is_valid += 1
        if is_valid == len(word):
            return True
        else:
            return False
        
    def put_word(self,word,pos,horizontal):
        if horizontal:
            for i in range(len(word)):
                self.grid[pos[0]-1][pos[1]-1+i].tile = word[i]
        else:
            for i in range(len(word)):
                self.grid[pos[0]-1+i][pos[1]-1].tile = word[i]

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