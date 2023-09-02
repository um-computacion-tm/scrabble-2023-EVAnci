import unittest
from game.cell import Cell
from game.bagtiles import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, letter_multiplier=True)
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.letter_multiplier,True)
        self.assertEqual(cell.active, True)
        self.assertIsNone(cell.tile)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, letter_multiplier=False)
        tile = Tile(letter='p', value=3)
        cell.add_letter(tile=tile)
        self.assertEqual(cell.tile, tile)

    def test_cell_value(self):
        cell = Cell(multiplier=2, letter_multiplier=True)
        tile = Tile(letter='p', value=3)
        cell.add_letter(tile=tile)
        self.assertEqual(cell.calculate_value(),6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, letter_multiplier=False)
        tile = Tile(letter='p', value=3)
        cell.add_letter(tile=tile)
        self.assertEqual(cell.calculate_value(),3)

    def test_cell_not_active(self):
        cell = Cell(multiplier=2, letter_multiplier=True, active=False)
        tile = Tile(letter='p', value=3)
        cell.add_letter(tile=tile)
        self.assertEqual(cell.calculate_value(),3)

if __name__ == '__main__':
    unittest.main()
