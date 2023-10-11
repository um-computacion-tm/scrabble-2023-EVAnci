import unittest
from unittest.mock import patch
from game.board import Board, NotInternetConnection
from game.bagtiles import Tile
from colorama import Fore, Back, Style, init

TRE = Back.RED + '     ' + Style.RESET_ALL 
TWO = Back.YELLOW + Fore.BLACK + '     ' + Style.RESET_ALL 
TRL = Back.BLUE + '     ' + Style.RESET_ALL 
TWL = Back.GREEN + '     ' + Style.RESET_ALL 
CEN = Back.GREEN + Fore.BLACK + f'  ✛  {Style.RESET_ALL}'

class TestBoard(unittest.TestCase):
    def test_board_constructor(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.is_empty(),True)
    
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        self.assertEqual(board.is_empty(),False)

    def test_put_word_h(self):
        board = Board()
        word = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location = (7, 7)
        horizontal = True
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[7][7+i].tile.letter
        self.assertEqual('CASA',word_in_board)

    def test_put_word_v(self):
        board = Board()
        word = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location = (7, 7)
        horizontal = False
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[7+i][7].tile.letter
        self.assertEqual('CASA',word_in_board)

    @patch('game.board.dle.search_by_word')
    def test_rae_search(self, mock_search_by_word):
        board = Board()
        valid_word = 'casa'
        mock_search_by_word.return_value.title = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        result1 = board.rae_search(valid_word)
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        invalid_word = 'uasffho'
        result2 = board.rae_search(invalid_word)
        self.assertEqual(result1, True)
        self.assertEqual(result2, False)

    @patch('game.board.dle.search_by_word')
    def test_rae_search_no_internet(self, mock_search_by_word):
        board = Board()
        valid_word = 'casa'
        mock_search_by_word.return_value = None
        with self.assertRaises(NotInternetConnection):
            board.rae_search(valid_word)

    def test_print_board(self):
        board = Board()
        actual_output = board.__repr__()
        expected_output = f'''
                                           TABLERO

       1     2     3     4     5     6     7     8     9    10    11    12    13    14    15
    ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
  1 │{TRE}│     │     │{TWL}│     │     │     │{TRE}│     │     │     │{TWL}│     │     │{TRE}│
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  2 │     │{TWO}│     │     │     │{TRL}│     │     │     │{TRL}│     │     │     │{TWO}│     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  3 │     │     │{TWO}│     │     │     │{TWL}│     │{TWL}│     │     │     │{TWO}│     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  4 │{TWL}│     │     │{TWO}│     │     │     │{TWL}│     │     │     │{TWO}│     │     │{TWL}│
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  5 │     │     │     │     │{TWO}│     │     │     │     │     │{TWO}│     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  6 │     │{TRL}│     │     │     │{TRL}│     │     │     │{TRL}│     │     │     │{TRL}│     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  7 │     │     │{TWL}│     │     │     │{TWL}│     │{TWL}│     │     │     │{TWL}│     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  8 │{TRE}│     │     │{TWL}│     │     │     │{CEN}│     │     │     │{TWL}│     │     │{TRE}│
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
  9 │     │     │{TWL}│     │     │     │{TWL}│     │{TWL}│     │     │     │{TWL}│     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 10 │     │{TRL}│     │     │     │{TRL}│     │     │     │{TRL}│     │     │     │{TRL}│     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 11 │     │     │     │     │{TWO}│     │     │     │     │     │{TWO}│     │     │     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 12 │{TWL}│     │     │{TWO}│     │     │     │{TWL}│     │     │     │{TWO}│     │     │{TWL}│
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 13 │     │     │{TWO}│     │     │     │{TWL}│     │{TWL}│     │     │     │{TWO}│     │     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 14 │     │{TWO}│     │     │     │{TRL}│     │     │     │{TRL}│     │     │     │{TWO}│     │
    ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤
 15 │{TRE}│     │     │{TWL}│     │     │     │{TRE}│     │     │     │{TWL}│     │     │{TRE}│
    └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘
{" "*20+Back.RED}3 Palabra{Style.RESET_ALL}{" "*8+Back.YELLOW+Fore.BLACK}2 Palabra{Style.RESET_ALL}{" "*8+Back.BLUE}3 Letra{Style.RESET_ALL}{" "*8+Back.GREEN}2 Letra{Style.RESET_ALL}'''
        self.maxDiff = None
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()