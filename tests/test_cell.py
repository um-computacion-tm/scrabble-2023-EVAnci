import unittest
from game.cell import Cell
from game.bagtiles import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, letter_multiplier=True)
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.letter_multiplier,True)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, letter_multiplier=False)
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, letter_multiplier=True)
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, letter_multiplier=False)
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3)

if __name__ == '__main__':
    unittest.main()
