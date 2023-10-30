import unittest
from unittest.mock import patch
from game.board import Board, NotInternetConnection
from game.bagtiles import Tile
from tests.graph import BOARD_OUTPUT

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

    def test_put_word_h_intersections(self):
        board = Board()
        board.grid[6][7].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',1)
        board.grid[9][7].tile = Tile('A',1)
        word = [Tile('L',3), Tile('S',6), Tile('O',1)]
        location = (7, 6)
        horizontal = True
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[7][6+i].tile.letter
        self.assertEqual('LASO',word_in_board)

    def test_put_word_v_intersections(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        word = [Tile('L',3), Tile('S',6), Tile('O',1)]
        location = (6, 7)
        horizontal = False
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[6+i][7].tile.letter
        self.assertEqual('LASO',word_in_board)

    def test_put_word_h_doble_intersections(self):
        board = Board()
        board.grid[6][7].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',1)
        board.grid[9][7].tile = Tile('A',1)
        board.grid[6][9].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('O',1)
        board.grid[8][9].tile = Tile('S',1)
        word = [Tile('L',3), Tile('S',6)]
        location = (7, 6)
        horizontal = True
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[7][6+i].tile.letter
        self.assertEqual('LASO',word_in_board)

    def test_put_word_v_doble_intersections(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        board.grid[9][6].tile = Tile('S',1)
        board.grid[9][7].tile = Tile('O',1)
        board.grid[9][8].tile = Tile('S',1)
        word = [Tile('L',3), Tile('S',6)]
        location = (6, 7)
        horizontal = False
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[6+i][7].tile.letter
        self.assertEqual('LASO',word_in_board)

    def test_put_word_add_a_letter_h(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        word = [Tile('S',1)]
        location = (7, 6)
        horizontal = True
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(5):
            word_in_board += board.grid[7][6+i].tile.letter
        self.assertEqual('CASAS',word_in_board)

    def test_put_word_add_a_letter_v(self):
        board = Board()
        board.grid[6][7].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',1)
        board.grid[9][7].tile = Tile('A',1)
        word = [Tile('S',1)]
        location = (6, 7)
        horizontal = False
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(5):
            word_in_board += board.grid[6+i][7].tile.letter
        self.assertEqual('CASAS',word_in_board)

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

    def test_get_word_without_intersections_no_intersected(self):
        board = Board()
        word = 'laso'
        pos = (6,7)
        horizontal = False
        result_word = board.get_word_without_intersections(word,pos,horizontal)
        self.assertEqual(result_word,'laso')

    def test_get_word_without_intersections_intersected(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        word = 'laso'
        pos = (6,7)
        horizontal = False
        result_word = board.get_word_without_intersections(word,pos,horizontal)
        self.assertEqual(result_word,'lso')

    def test_print_board(self):
        board = Board()
        actual_output = board.__repr__()
        expected_output = BOARD_OUTPUT
        self.maxDiff = None
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()