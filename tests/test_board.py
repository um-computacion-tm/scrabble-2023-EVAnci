import unittest
from game.board import Board
from game.bagtiles import Tile

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
        word_is_valid = board.validate(word, location, horizontal)
        assert word_is_valid == True
    
    def test_word_out_of_board_h(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        horizontal = True
        word_is_valid = board.validate(word, location, horizontal)
        assert word_is_valid == False

    def test_word_inside_board_v(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        horizontal = False
        word_is_valid = board.validate(word, location, horizontal)
        assert word_is_valid == True
    
    def test_word_out_of_board_v(self):
        board = Board()
        word = "Facultad"
        location = (5, 14)
        horizontal = False
        word_is_valid = board.validate(word, location, horizontal)
        assert word_is_valid == False

    def test_put_word_h(self):
        board = Board()
        word = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location = (5, 4)
        horizontal = True
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[4][3+i].tile.letter
        self.assertEqual('CASA',word_in_board)

    def test_put_word_v(self):
        board = Board()
        word = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location = (5, 4)
        horizontal = False
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[4+i][3].tile.letter
        self.assertEqual('CASA',word_in_board)

    def test_validate_word_with_previous_word(self):
        board = Board()
        word_1 = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location_1 = (5, 4)
        horizontal_1 = True
        board.put_word(word_1,location_1,horizontal_1)
        word_2 = [Tile('L',3), Tile('A',1), Tile('S',6), Tile('O',1)]
        location_2 = (5, 4)
        horizontal_2 = False
        word_is_valid = board.validate(word_2,location_2,horizontal_2)
        assert word_is_valid == False

    def test_validate_word_with_different_pos_previous_word(self):
        board = Board()
        word_1 = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location_1 = (5, 4)
        horizontal_1 = True
        board.put_word(word_1,location_1,horizontal_1)
        word_2 = 'LASO'
        location_2 = (6, 4)
        horizontal_2 = False
        word_is_valid = board.validate(word_2,location_2,horizontal_2)
        assert word_is_valid == True

    def test_validate_word_with_same_previous_letter(self):
        board = Board()
        word_1 = [Tile('C',3), Tile('A',1), Tile('S',6), Tile('A',1)]
        location_1 = (5, 4)
        horizontal_1 = True
        board.put_word(word_1,location_1,horizontal_1)
        word_2 = 'LASO'
        location_2 = (4, 5)
        horizontal_2 = False
        word_is_valid = board.validate(word_2,location_2,horizontal_2)
        self.assertEqual(word_is_valid, True)

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