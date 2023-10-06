import unittest
from unittest.mock import patch
from game.board import Board, NotInternetConnection
from game.bagtiles import Tile

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
        expected_output = '''                  TABLERO

        A B C D E F G H I J K L M N O 
  1  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  2  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  3  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  4  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  5  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  6  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  7  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  8  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
  9  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 10  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 11  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 12  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 13  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 14  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
 15  |  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

'''
        self.maxDiff = None
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()