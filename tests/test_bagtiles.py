import unittest
from unittest.mock import patch
from game.bagtiles import (
    BagTiles,
    Tile,
    Wildcard,
    TOTAL_TILES,
    InsufficientTiles,
    BagIsFull
)

class TestTile(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_repr(self):
        tile = Tile('A',1)
        self.assertEqual(tile.__repr__(), 'A')

class TestWildcardTile(unittest.TestCase):
    def test_wildcard(self):
        wildcard = Wildcard()
        self.assertEqual(wildcard.letter, '?')
        self.assertEqual(wildcard.value, 0)

    def test_select_wildcard_letter(self):
        wildcard = Wildcard()
        wildcard.select_letter('a')
        self.assertEqual(wildcard.letter, 'A')
        self.assertEqual(wildcard.value, 0)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle') # Mock random.shuffle function
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), TOTAL_TILES)
        self.assertEqual(patch_shuffle.call_count, 1) # Check it's called once
        self.assertEqual(patch_shuffle.call_args[0][0], bag.tiles) 

    def test_take(self):
        bag = BagTiles()
        tiles_taken = bag.take(2)
        self.assertEqual(len(bag.tiles), TOTAL_TILES-2)
        self.assertEqual(len(tiles_taken), 2)

    def test_take_cero(self):
        bag = BagTiles()
        tiles_taken = bag.take(0)
        self.assertEqual(len(bag.tiles), TOTAL_TILES)
        self.assertEqual(len(tiles_taken), 0)

    def test_take_empty(self):
        bag = BagTiles()
        bag.take(TOTAL_TILES)
        with self.assertRaises(InsufficientTiles):
            bag.take(1)

    def test_take_invalid(self):
        bag = BagTiles()
        bag.take(97)
        with self.assertRaises(InsufficientTiles):
            bag.take(4)

    def test_put_one(self):
        bag = BagTiles()
        taken = bag.take(7)
        self.assertEqual(len(bag.tiles), TOTAL_TILES-7)
        put_tiles = [taken[0]]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), TOTAL_TILES-6)

    def test_put_tree(self):
        bag = BagTiles()
        taken = bag.take(7) 
        self.assertEqual(len(bag.tiles), TOTAL_TILES-7)
        put_tiles = [taken[1], taken[2], taken[4]]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), TOTAL_TILES-4)

    def test_put_with_full_bag(self):
        bag = BagTiles()
        with self.assertRaises(BagIsFull):
            bag.put([Tile('A', 1)])

if __name__ == '__main__':
    unittest.main()
