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

    def test_horizontal_left_pos(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(7,4),horizontal=True)
        self.assertEqual(result, True)
    
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

    def test_horizontal_upper_pos(self):
        board = Board()
        word = 'CASA'
        result = board.validate_empty(word,pos=(4,7),horizontal=False)
        self.assertEqual(result, True)

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

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_valid_right(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'soso, sosa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('A',1)
        board.grid[6][9].tile = Tile('L',3)
        board.grid[8][9].tile = Tile('S',6)
        board.grid[9][9].tile = Tile('O',1)
        board.grid[9][8].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('O',1)
        word = 'cosa'
        horizontal = False
        pos = (7,6)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, True)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_invalid_right(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('A',1)
        board.grid[6][9].tile = Tile('L',3)
        board.grid[8][9].tile = Tile('S',6)
        board.grid[9][9].tile = Tile('O',1)
        board.grid[9][8].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('O',1)
        word = 'cono'
        horizontal = False
        pos = (7,6)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, False)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_valid_left(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'osos | Definición | Diccionario de la lengua española | RAE - ASALE'  
        board = Board()
        board.grid[7][4].tile = Tile('C',3)
        board.grid[7][5].tile = Tile('A',1)
        board.grid[7][6].tile = Tile('S',6)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',6)
        board.grid[6][5].tile = Tile('L',3)
        board.grid[8][5].tile = Tile('S',6)
        board.grid[9][5].tile = Tile('O',1)
        board.grid[9][6].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('O',1)
        word = 'casos'
        horizontal = False
        pos = (5,8)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, True)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_invalid_left(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        board = Board()
        board.grid[7][4].tile = Tile('C',3)
        board.grid[7][5].tile = Tile('A',1)
        board.grid[7][6].tile = Tile('S',6)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',6)
        board.grid[6][5].tile = Tile('L',3)
        board.grid[8][5].tile = Tile('S',6)
        board.grid[9][5].tile = Tile('O',1)
        board.grid[9][6].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('O',1)
        word = 'sopa'
        horizontal = False
        pos = (7,8)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, False)

    # @patch('game.board.dle.search_by_word')
    # def test_two_complex_word_validation_valid_left(self, mock_search_by_word):
    #     mock_search_by_word.return_value.title = 'osos | Definición | Diccionario de la lengua española | RAE - ASALE'  
    #     mock_search_by_word.return_value.title = 'casas | Definición | Diccionario de la lengua española | RAE - ASALE'  
    #     board = Board()
    #     board.grid[7][4].tile = Tile('C',3)
    #     board.grid[7][5].tile = Tile('A',1)
    #     board.grid[7][6].tile = Tile('S',6)
    #     board.grid[7][7].tile = Tile('A',1)
    #     board.grid[6][5].tile = Tile('L',3)
    #     board.grid[8][5].tile = Tile('S',6)
    #     board.grid[9][5].tile = Tile('O',1)
    #     board.grid[9][6].tile = Tile('S',6)
    #     board.grid[9][7].tile = Tile('O',1)
    #     word = 'casos'
    #     horizontal = False
    #     pos = (5,8)
    #     is_valid = board.validate_not_empty(word, pos, horizontal)
    #     self.assertEqual(is_valid, True)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_valid_lower(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'soso, sosa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[6][7].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('A',1)
        board.grid[9][6].tile = Tile('L',3)
        board.grid[9][8].tile = Tile('S',6)
        board.grid[9][9].tile = Tile('O',1)
        board.grid[8][9].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('O',1)
        word = 'cosa'
        horizontal = True
        pos = (6,7)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, True)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_invalid_lower(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        board = Board()
        board.grid[6][7].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',6)
        board.grid[9][7].tile = Tile('A',1)
        board.grid[9][6].tile = Tile('L',3)
        board.grid[9][8].tile = Tile('S',6)
        board.grid[9][9].tile = Tile('O',1)
        board.grid[8][9].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('O',1)
        word = 'cono'
        horizontal = True
        pos = (6,7)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        self.assertEqual(is_valid, False)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_valid_up(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'osos | Definición | Diccionario de la lengua española | RAE - ASALE'  
        board = Board()
        board.grid[4][7].tile = Tile('C',3)
        board.grid[5][7].tile = Tile('A',1)
        board.grid[6][7].tile = Tile('S',6)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',6)
        board.grid[5][6].tile = Tile('L',3)
        board.grid[5][8].tile = Tile('S',6)
        board.grid[5][9].tile = Tile('O',1)
        board.grid[6][9].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('O',1)
        # print(board.view())
        word = 'casos'
        horizontal = True
        pos = (8,5)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        # board.put_word([Tile('C',1),Tile('A',1),Tile('S',1),Tile('O',1),Tile('S',1)],pos,horizontal)
        # print(board.view())
        self.assertEqual(is_valid, True)

    @patch('game.board.dle.search_by_word')
    def test_complex_word_validation_invalid_up(self, mock_search_by_word):
        mock_search_by_word.return_value.title = 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'  
        board = Board()
        board.grid[4][7].tile = Tile('C',3)
        board.grid[5][7].tile = Tile('A',1)
        board.grid[6][7].tile = Tile('S',6)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[8][7].tile = Tile('S',6)
        board.grid[5][6].tile = Tile('L',3)
        board.grid[5][8].tile = Tile('S',6)
        board.grid[5][9].tile = Tile('O',1)
        board.grid[6][9].tile = Tile('S',6)
        board.grid[7][9].tile = Tile('O',1)
        word = 'sopa'
        horizontal = True
        pos = (8,7)
        is_valid = board.validate_not_empty(word, pos, horizontal)
        # board.put_word([Tile('S',1),Tile('O',1),Tile('P',1),Tile('A',1)],pos,horizontal)
        # print(board.view())
        self.assertEqual(is_valid, False)

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