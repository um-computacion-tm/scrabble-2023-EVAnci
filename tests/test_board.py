import unittest
from game.board import Board

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)
    
    def test_word_inside_board_h(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        horizontal = True
        word_is_valid = board.validate_word_inside_board(word, location, horizontal)
        assert word_is_valid == True
    
    def test_word_out_of_board_h(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        horizontal = True
        word_is_valid = board.validate_word_inside_board(word, location, horizontal)
        assert word_is_valid == False

    def test_word_inside_board_v(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        horizontal = False
        word_is_valid = board.validate_word_inside_board(word, location, horizontal)
        assert word_is_valid == True
    
    def test_word_out_of_board_v(self):
        board = Board()
        word = "Facultad"
        location = (5, 14)
        horizontal = False
        word_is_valid = board.validate_word_inside_board(word, location, horizontal)
        assert word_is_valid == False

    def test_print_board(self):
        board = Board()
        actual_output = board.view()
        expected_output = '''                  TABLERO

        A B C D E F G H I J K L M N L 
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