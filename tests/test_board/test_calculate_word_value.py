import unittest
from game.board import Board
from game.bagtiles import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()        
        word = 'casa'
        pos=(10,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 6)

    def test_simple_with_double_letter(self):
        board = Board()
        word = 'lluvia'
        pos=(10,5)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 8+1+4+1+1)
        
    def test_with_word_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(7,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 12)

    def test_with_word_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(14,6)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 18)

    def test_with_letter_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(8,8)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 9)

    def test_with_letter_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(9,8)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 8)

    def test_with_letter_multiplier_and_word_multiplier(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 21)

    def test_with_letter_multiplier_and_word_multiplier_no_active(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, horizontal=True)
        value = board.calculate_word_value(word, pos, horizontal=True)
        self.assertEqual(value, 6)

    def test_simple_intersection(self):
        board = Board()
        board.grid[7][2].tile = Tile('E', 1)
        board.grid[7][3].tile = Tile('S', 1)
        board.grid[7][4].tile = Tile('T', 1)
        board.grid[7][5].tile = Tile('R', 1)
        board.grid[7][6].tile = Tile('E', 1)
        board.grid[7][7].tile = Tile('N', 1)
        board.grid[7][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'mes'
        pos=(6,6)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 21)

    def test_simple_intersection_inverted(self):
        board = Board()
        board.grid[7][2].tile = Tile('E', 1)
        board.grid[7][3].tile = Tile('S', 1)
        board.grid[7][4].tile = Tile('T', 1)
        board.grid[7][5].tile = Tile('R', 1)
        board.grid[7][6].tile = Tile('E', 1)
        board.grid[7][7].tile = Tile('N', 1)
        board.grid[7][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'mes'
        pos=(8,6)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 21)

    def test_simple_intersection_2(self):
        board = Board()
        board.grid[7][5].tile = Tile('C', 3)
        board.grid[7][6].tile = Tile('A', 1)
        board.grid[7][7].tile = Tile('S', 1)
        board.grid[7][8].tile = Tile('A', 1)
        board.grid[6][8].tile = Tile('L', 1)
        board.grid[8][8].tile = Tile('S', 1)
        board.grid[9][8].tile = Tile('O', 1)
        board.grid[9][7].tile = Tile('S', 1)
        board.grid[9][6].tile = Tile('O', 1)
        word = 'cosa'
        pos=(7,5)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 14)

    def test_simple_intersection_inverted_2(self):
        board = Board()
        board.grid[7][5].tile = Tile('C', 3)
        board.grid[7][6].tile = Tile('A', 1)
        board.grid[7][7].tile = Tile('S', 1)
        board.grid[7][8].tile = Tile('A', 1)
        board.grid[8][5].tile = Tile('O', 1)
        board.grid[9][5].tile = Tile('S', 1)
        board.grid[10][5].tile = Tile('A', 1)
        board.grid[9][7].tile = Tile('S', 1)
        board.grid[9][6].tile = Tile('O', 1)
        board.grid[9][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        word = 'laso'
        pos=(5,9)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 13)

    def test_simple_intersection_inverted_3(self):
        board = Board()
        board.grid[7][5].tile = Tile('C', 3)
        board.grid[7][6].tile = Tile('A', 1)
        board.grid[7][7].tile = Tile('S', 1)
        board.grid[7][8].tile = Tile('A', 1)
        board.grid[8][5].tile = Tile('O', 1)
        board.grid[9][5].tile = Tile('S', 1)
        board.grid[10][5].tile = Tile('A', 1)
        board.grid[9][7].tile = Tile('S', 1)
        board.grid[9][6].tile = Tile('O', 1)
        board.grid[9][8].tile = Tile('O', 1)
        board.grid[7][7].active = False
        board.grid[9][5].active = False
        word = 'lasos'
        pos=(5,9)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 23)

    def test_out_of_range_side(self):
        board = Board()
        word = 'casa'
        pos = (14,10)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        pos = (0,0)
        horizontal = True
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value!=None, True)

    def test_letter_not_available(self):
        board = Board()
        word = 'c?sa'
        pos = (7,7)
        horizontal = True
        value = board.calculate_word_value(word,pos,horizontal)
        self.assertEqual(value, 10)

if __name__ == '__main__':
    unittest.main()