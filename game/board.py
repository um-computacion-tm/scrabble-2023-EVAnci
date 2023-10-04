from game.cell import Cell
from pyrae import dle

class NotInternetConnection(Exception):
    pass

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

    def is_empty(self):
        if self.grid[7][7].tile is None:
            return True
        return False

    def validate_empty(self, word, pos, horizontal):
        row = pos[0]
        column = pos[1]
        for i in range(len(word)):
            if row == 7 and column == 7:
                return True
            if horizontal:
                column += 1
            else:
                row +=1
        return False

    def horizontal_validation(self, word, pos):
        intersections = 0
        is_valid = 0
        for i in range(len(word)):
            cell = self.grid[pos[0]][pos[1]+i].tile
            # uppercell = self.grid[pos[0]-1][pos[1]+i].tile
            # lowercell = self.grid[pos[0]+1][pos[1]+i].tile
            # word2_is_valid = True
            if cell is not None:
                intersections += 1
                if cell.letter == word[i]:
                    is_valid += 1
        return (is_valid, intersections)

    def vertical_validation(self, word, pos):
        intersections = 0
        is_valid = 0
        for i in range(len(word)):
            cell = self.grid[pos[0]+i][pos[1]].tile
            leftcell = self.grid[pos[0]+i][pos[1]-1].tile
            rightcell = self.grid[pos[0]+i][pos[1]+1].tile
            word2_is_valid = True
            if rightcell is not None and cell is None:
                word2 = word[i]
                index = 1
                while rightcell is not None:
                    word2 += rightcell.letter.lower()
                    rightcell = self.grid[pos[0]+i][pos[1]+1+index].tile
                    index += 1
                word2_is_valid = "Definición" in dle.search_by_word(word2).title
                if not word2_is_valid:
                    is_valid = -9999
            elif leftcell is not None and cell is None:
                word2 = word[i]
                index = 1
                while leftcell is not None:
                    word2 += leftcell.letter.lower()
                    leftcell = self.grid[pos[0]+i][pos[1]-1-index].tile
                    index += 1
                word2 = word2[::-1]
                word2_is_valid = "Definición" in dle.search_by_word(word2).title
                if not word2_is_valid:
                    is_valid = -9999
            if cell is not None:
                intersections += 1
                if cell.letter == word[i].upper():
                    is_valid += 1
        return (is_valid, intersections)

    def validate_not_empty(self, word, pos, horizontal):
        h_space = len(word) <= len(self.grid)-pos[0]
        v_space = len(word) <= len(self.grid)-pos[1]
        if (horizontal and h_space):
            is_valid = self.horizontal_validation(word,pos)
        elif ((not horizontal) and v_space):
            is_valid = self.vertical_validation(word,pos)
        if is_valid[0] != 0 and is_valid[1] == is_valid[0]:
            return True
        else:
            return False

    def validate(self, word, pos, horizontal):
        rae = dle.search_by_word(word)
        if rae == None:
            raise NotInternetConnection
        if 'Definición' in rae.title:
            if self.is_empty():
                return self.validate_empty(word, pos, horizontal)
            else:
                return self.validate_not_empty(word, pos, horizontal)
        return False

    def put_word(self,word,pos,horizontal):
        if horizontal:
            for i in range(len(word)):
                self.grid[pos[0]][pos[1]+i].tile = word[i]
        else:
            for i in range(len(word)):
                self.grid[pos[0]+i][pos[1]].tile = word[i]

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