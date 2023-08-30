import unittest
from game.board import Board
from game.cell import Cell
from game.bagtiles import Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        cell_1 = Cell(multiplier=1,letter_multiplier=False)
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,letter_multiplier=False)
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=1,letter_multiplier=False)
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,letter_multiplier=False)
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        cell_1 = Cell(multiplier=1,letter_multiplier=False)
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,letter_multiplier=False)
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,letter_multiplier=True)
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,letter_multiplier=False)
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell_1 = Cell(multiplier=1,letter_multiplier=False)
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,letter_multiplier=False)
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,letter_multiplier=False)
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,letter_multiplier=False)
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell_1 = Cell(multiplier=3,letter_multiplier=True)
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,letter_multiplier=False)
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,letter_multiplier=False)
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,letter_multiplier=False)
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        cell_1 = Cell(multiplier=3,letter_multiplier=True,active=False)
        cell_1.add_letter(Tile('C', 1)) 
        cell_2 = Cell(multiplier=1,letter_multiplier=False,active=False)
        cell_2.add_letter(Tile('A', 1))
        cell_3 = Cell(multiplier=2,letter_multiplier=False,active=False)
        cell_3.add_letter(Tile('S', 2))
        cell_4 = Cell(multiplier=1,letter_multiplier=False,active=False)
        cell_4.add_letter(Tile('A', 1))

        word = [cell_1, cell_2, cell_3, cell_4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)

if __name__ == '__main__':
    unittest.main()
