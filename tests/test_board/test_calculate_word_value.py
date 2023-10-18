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
        word = 'tres'
        pos=(7,4)
        horizontal = False
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value, 8)


if __name__ == '__main__':
    unittest.main()