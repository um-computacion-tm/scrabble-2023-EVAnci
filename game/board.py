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
    
    def rae_search(self, word):
        rae = dle.search_by_word(word)
        if rae is None:
            raise NotInternetConnection
        return 'D' != rae.title[:1]

    def is_empty(self):
        return self.grid[7][7].tile is None

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
        grid = self.grid
        def validate_side_cell(cell, index_increment):
            nonlocal is_valid, intersections
            word2 = word[i]
            index = 1
            while cell:
                word2 += cell.letter.lower()
                side_words.append(cell)
                cell = grid[pos[0] + index_increment * index][pos[1] + i].tile
                index += 1
            word2_is_valid = self.rae_search(word2)
            if not word2_is_valid:
                is_valid = -9999
            else:
                is_valid += 1
                intersections += 1
        for i in range(len(word)):
            cell = self.grid[pos[0]][pos[1] + i].tile
            uppercell = self.grid[pos[0] - 1][pos[1] + i].tile
            lowercell = self.grid[pos[0] + 1][pos[1] + i].tile
            word2_is_valid = True
            side_words = []
            if cell:
                intersections += 1
                if cell.letter == word[i].upper():
                    is_valid += 1
            elif lowercell:
                validate_side_cell(lowercell, 1)
                if is_valid == -9999:
                    break
            elif uppercell:
                validate_side_cell(uppercell, -1)
                if is_valid == -9999:
                    break    
        return (is_valid, intersections)

    def vertical_validation(self, word, pos):
        intersections = 0
        is_valid = 0
        grid = self.grid
        def validate_side_cell(cell, index_increment):
            nonlocal is_valid, intersections
            word2 = word[i]
            index = 1
            while cell:
                word2 += cell.letter.lower()
                side_words.append(cell)
                cell = grid[pos[0] + i][pos[1] + index_increment * index].tile
                index += 1
            word2_is_valid = self.rae_search(word2)
            if not word2_is_valid:
                is_valid = -9999
            else:
                is_valid += 1
                intersections += 1
        for i in range(len(word)):
            cell = grid[pos[0] + i][pos[1]].tile
            leftcell = grid[pos[0] + i][pos[1] - 1].tile
            rightcell = grid[pos[0] + i][pos[1] + 1].tile
            word2_is_valid = True
            side_words = []
            if cell:
                intersections += 1
                if cell.letter == word[i].upper():
                    is_valid += 1
            elif rightcell:
                validate_side_cell(rightcell, 1)
                if is_valid == -9999:
                    break
            elif leftcell:
                validate_side_cell(leftcell, -1)
                if is_valid == -9999:
                    break
        return is_valid, intersections

    def validate_not_empty(self, word, pos, horizontal):
        h_space = len(word) <= len(self.grid)-pos[0]
        v_space = len(word) <= len(self.grid)-pos[1]
        intersections = 0
        is_valid = 0
        grid = self.grid
        def validate_side_cell(cell, index_increment):
            nonlocal is_valid, intersections
            word2 = word[i]
            index = 1
            while cell:
                word2 += cell.letter.lower()
                side_words.append(cell)
                cell = grid[pos[0] + i + index_increment * index][pos[1] + i].tile
                index += 1
            word2_is_valid = self.rae_search(word2)
            if not word2_is_valid:
                is_valid = -9999
            else:
                is_valid += 1
                intersections += 1

        for i in range(len(word)):
            cell = grid[pos[0] + (i if horizontal else 0)][pos[1] + (i if not horizontal else 0)].tile
            leftcell = grid[pos[0] + i][pos[1] - 1].tile if not horizontal else None
            rightcell = grid[pos[0] + i][pos[1] + 1].tile if not horizontal else None
            uppercell = grid[pos[0] - 1][pos[1] + i].tile if horizontal else None
            lowercell = grid[pos[0] + 1][pos[1] + i].tile if horizontal else None
            word2_is_valid = True
            side_words = []
            if cell:
                intersections += 1
                if cell.letter == word[i].upper():
                    is_valid += 1
            elif (horizontal and lowercell) or (not horizontal and rightcell):
                validate_side_cell(lowercell if horizontal else rightcell, 1)
                if is_valid == -9999:
                    break
            elif (horizontal and uppercell) or (not horizontal and leftcell):
                validate_side_cell(uppercell if horizontal else leftcell, -1)
                if is_valid == -9999:
                    break

        if is_valid != 0 and is_valid == intersections:
            return True
        else:
            return False

    def validate(self, word, pos, horizontal):
        rae = dle.search_by_word(word)
        if rae == None:
            raise NotInternetConnection
        if 'Diccionario' not in rae.title[:11]:
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