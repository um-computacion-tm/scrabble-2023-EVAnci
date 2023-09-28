import unittest
from unittest.mock import patch
from game.board import Board, NotInternetConnection
from game.bagtiles import Tile

class Test_Validate_empty(unittest.TestCase):
    def test_horizontal_centred(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(7,7),horizontal=True)
        self.assertEqual(result, True)

    def test_horizontal_not_centred(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(8,7),horizontal=True)
        self.assertEqual(result, False)
    
    def test_horizontal_out_of_range(self):
        board = Board()
        word = 'FACULTADES'
        result = board.validate_empty(word,pos=(7,7),horizontal=True)
        self.assertEqual(result, False)

    def test_vertical_centred(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(7,7),horizontal=False)
        self.assertEqual(result, True)

    def test_vertical_not_centred(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(7,8),horizontal=False)
        self.assertEqual(result, False)

    def test_vertical_out_of_range(self):
        board = Board()
        word = 'FACULTADES'
        result = board.validate_empty(word,pos=(7,7),horizontal=False)
        self.assertEqual(result, False)

class Test_Validate_not_empty(unittest.TestCase):
    def test_one_valid_intesection(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        word = 'LASO'
        result = board.validate_not_empty(word,pos=(6,10),horizontal=False)
        self.assertEqual(result, True)

    def test_one_invalid_intesection(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        word = 'LASO'
        result = board.validate_not_empty(word,pos=(5,10),horizontal=False)
        self.assertEqual(result, False)

    def test_one_not_intesection(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        word = 'LASO'
        result = board.validate_not_empty(word,pos=(0,10),horizontal=False)
        self.assertEqual(result, False)

    def test_word_of_word_valid(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        word = 'CASAS'
        result = board.validate_not_empty(word,pos=(7,7),horizontal=True)
        self.assertEqual(result, True)

    def test_word_of_word_invalid(self):
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        word = 'CASOS'
        result = board.validate_not_empty(word,pos=(7,7),horizontal=True)
        self.assertEqual(result, False)

class Test_Validate(unittest.TestCase):
    @patch('game.board.dle.search_by_word')
    def test_invalid_word(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'
        board = Board()
        result = board.validate(word='YOAS',pos=(7,7),horizontal=True)
        self.assertEqual(result, False)

    @patch('game.board.dle.search_by_word')
    def test_valid_word_empty(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        result = board.validate(word='CASA',pos=(7,7),horizontal=True)
        self.assertEqual(result, True)

    @patch('game.board.dle.search_by_word')
    def test_valid_word_not_empty(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'laso, lasa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].tile = Tile('C',3)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',6)
        board.grid[7][10].tile = Tile('A',1)
        result = board.validate(word='LASO',pos=(6,10),horizontal=False)
        self.assertEqual(result, True)

    @patch('game.board.dle.search_by_word')
    def test_validate_not_internet_connection(self, mock_search_by_word):
        mock_search_by_word.return_value = None
        board = Board()
        with self.assertRaises(NotInternetConnection):
            board.validate(word='CASA',pos=(7,7),horizontal=True)

if __name__ == '__main__':
    unittest.main()