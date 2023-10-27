from game.cell import Cell
from game.player import Player
from game.bagtiles import DATA
from pyrae import dle
from colorama import Fore, Back, Style, init

class NotInternetConnection(Exception):
    pass

class Board():
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]
        dle.set_log_level(log_level='CRITICAL')
        # Local function to put multipiers
        def put_bonus(pos_list, bonus_type):
            for pos in pos_list:
                self.grid[pos[0]][pos[1]] = Cell(multiplier=bonus_type[0], letter_multiplier=bonus_type[1])
                self.grid[pos[0]][14-pos[1]] = Cell(multiplier=bonus_type[0], letter_multiplier=bonus_type[1])
                self.grid[14-pos[0]][pos[1]] = Cell(multiplier=bonus_type[0], letter_multiplier=bonus_type[1])
                self.grid[14-pos[0]][14-pos[1]] = Cell(multiplier=bonus_type[0], letter_multiplier=bonus_type[1])
        pos_list = [(0,0), (0,7), (7,0)]
        put_bonus(pos_list, (3, False))
        pos_list = [(1,1), (2,2), (3,3), (4,4), (7,7)]
        put_bonus(pos_list, (2, False))
        pos_list = [(5,1), (5,5), (1,5)]
        put_bonus(pos_list, (3, True))
        pos_list = [(0,3), (3,0), (2,6), (6,2), (7, 3), (3, 7), (6, 6)]
        put_bonus(pos_list, (2, True))

    def calculate_word_value(self, word, pos, horizontal, first=True):
        word = Player().split_word(word)
        points = 0
        word_multiplier = 1
        i = 0

        for letter in word:
            cell, invert_cell, side_cell = self.get_cells(pos, i, horizontal)
            available = not cell.tile and first
            j = 1

            if invert_cell and invert_cell.tile and available:
                side_word, j = self.get_side_word(invert_cell, i, (horizontal,True), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0] - j + 1, pos[1] + i) if horizontal else (pos[0] + i, pos[1] - j + 1), not horizontal, False)
            elif side_cell and side_cell.tile and available:
                side_word, j = self.get_side_word(side_cell, i, (horizontal,False), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0], pos[1] + i) if horizontal else (pos[0] + i, pos[1]), not horizontal, False)
            letter_value = self.get_letter_value(letter)
            word_multiplier, points = self.update_multipliers(cell, letter_value, word_multiplier, points, first)
            i += 1

        points = points * word_multiplier
        return points

    def get_cells(self, pos, i, horizontal):
        cell = self.grid[pos[0]][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1]]
        if pos[0] > 0 and pos[1] > 0:
            invert_cell = self.grid[pos[0] - 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] - 1]
        else:
            invert_cell = None
        try:
            side_cell = self.grid[pos[0] + 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + 1]
        except:
            side_cell = None
        return cell, invert_cell, side_cell

    def get_side_word(self, cell, i, orientation, pos, letter):
        horizontal = orientation[0]
        inverted = orientation[1]
        k = -1 if inverted else 1
        side_word = letter
        j = 1
        # print(f'Initial pos {pos}')
        while cell.tile:
            side_word += cell.tile.letter
            cell = self.grid[pos[0] + (1 + j)*k][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + (1 + j)*k]
            j += 1
            # print(f'Position {(pos[0] + i,pos[1] - 1 - j)}; Inverted {inverted}; Horizontal {horizontal}')
        if inverted:
            side_word = side_word[::-1]
        return side_word, j

    def get_letter_value(self, letter):
        for tile in DATA:
            if letter == tile['letter']:
                return tile['points']
        return 0

    def update_multipliers(self, cell, letter_value, word_multiplier, points, first):
        if not (cell.letter_multiplier) and cell.active:
            word_multiplier *= cell.multiplier

        if cell.letter_multiplier and cell.active:
            points += letter_value * cell.multiplier
        else:
            points += letter_value

        if first:
            cell.active = False

        return word_multiplier, points
    
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

    def validate_not_empty(self, word, pos, horizontal):
        intersections = 0
        is_valid = 0
        grid = self.grid
        def validate_side_cell(cell, index_increment):
            nonlocal is_valid, intersections
            word2 = word[i]
            index = 1
            while cell:
                word2 += cell.letter.lower()
                cell = grid[pos[0] + i + index_increment * index][pos[1] + i].tile
                index += 1
            word2_is_valid = self.rae_search(word2)
            if not word2_is_valid:
                is_valid = -9999
            else:
                is_valid += 1
                intersections += 1
        for i in range(len(word)):
            cell = grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].tile
            leftcell = grid[pos[0] + i][pos[1] - 1].tile if not horizontal else None
            rightcell = grid[pos[0] + i][pos[1] + 1].tile if not horizontal else None
            uppercell = grid[pos[0] - 1][pos[1] + i].tile if horizontal else None
            lowercell = grid[pos[0] + 1][pos[1] + i].tile if horizontal else None
            if cell:
                intersections += 1
                if cell.letter == word[i].upper():
                    is_valid += 1
            elif (horizontal and lowercell) or (not horizontal and rightcell):
                validate_side_cell(lowercell if horizontal else rightcell, 1)
                if is_valid < 0:
                    break
            elif (horizontal and uppercell) or (not horizontal and leftcell):
                validate_side_cell(uppercell if horizontal else leftcell, -1)
                if is_valid < 0:
                    break
        if is_valid != 0 and is_valid == intersections:
            return True
        return False

    def validate(self, word, pos, horizontal):
        if self.rae_search(word):
            if self.is_empty():
                return self.validate_empty(word, pos, horizontal)
            else:
                return self.validate_not_empty(word, pos, horizontal)
        return False

    def get_word_without_intersections(self,word,pos,horizontal):
        result = ''
        for i in range(len(word)):
            cell = self.grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].tile
            if not cell:
                result += word[i]
        return result

    def put_word(self,word,pos,horizontal):
        j=0
        for i in range(len(word)):
            cell = self.grid[pos[0]][pos[1]+i+j] if horizontal else self.grid[pos[0]+i+j][pos[1]]
            if not cell.tile:
                cell.tile = word[i]
            else:
                cell = self.grid[pos[0]][pos[1]+i+1] if horizontal else self.grid[pos[0]+i+1][pos[1]]
                cell.tile = word[i]
                j+=1


    def repr_wrapper(self,view, row):
        for column in range(15):
            cell = self.grid[row][column]
            if row == 7 and column == 7 and cell.tile == None:
                view += Back.YELLOW + Fore.BLACK + f'  ✛  {Style.RESET_ALL}│' 
            else:
                if not cell.letter_multiplier and cell.multiplier == 3:
                    view += Back.RED + cell.__repr__().center(5, ' ') + Style.RESET_ALL + '│' 
                elif not cell.letter_multiplier and cell.multiplier == 2:
                    view += Back.YELLOW + Fore.BLACK + cell.__repr__().center(5, ' ') + Style.RESET_ALL + '│' 
                elif cell.letter_multiplier and cell.multiplier == 3:
                    view += Back.BLUE + cell.__repr__().center(5, ' ') + Style.RESET_ALL + '│' 
                elif cell.letter_multiplier and cell.multiplier == 2:
                    view += Back.GREEN + cell.__repr__().center(5, ' ') + Style.RESET_ALL + '│' 
                else:
                    view += cell.__repr__().center(5, ' ') + '│'
            view += '\n' if column == 14 else ''
        return view

    def __repr__(self):
        init()
        view = (f'\n{" "*43}TABLERO\n\n')
        index = ('       1     2     3     4     5     6     7     8     9    10    11    12    13    14    15\n')
        view += (index + '    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐\n')
        for row in range(15):
            #if the number is higher than 2 digits, then
            # you need to erase an space for correct formatting
            if row+1 < 10:
                view += (f'  {row+1} ')
            else:
                view += (f' {row+1} ')
            view += '│' 
            view = self.repr_wrapper(view, row)
            if row != 14:
                view += '    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤\n'
            else:
                view += '    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘\n'
                view += f'{" "*20+Back.RED}3 Palabra{Style.RESET_ALL}{" "*8+Back.YELLOW+Fore.BLACK}2 Palabra{Style.RESET_ALL}{" "*8+Back.BLUE}3 Letra{Style.RESET_ALL}{" "*8+Back.GREEN}2 Letra{Style.RESET_ALL}'
        return view