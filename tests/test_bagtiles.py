####################
#     Imports      #
####################

import unittest
from game.bagtiles import (
    BagTiles,
    Tile,
    TOTAL_TILES,
    PutBagFullException,
    TakeBagEmptyException
)
from unittest.mock import patch

####################
#      Tests       #
####################

class TestTilesCreation(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), TOTAL_TILES)
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.tiles)

    def test_take(self):
        bag = BagTiles()
        tiles_taken = bag.take(2)
        self.assertEqual(len(bag.tiles), TOTAL_TILES-2)
        self.assertEqual(len(tiles_taken), 2)

    def test_take_empty(self):
        bag = BagTiles()
        bag.take(TOTAL_TILES)
        self.assertEqual([], bag.take(1))

    def test_put_one(self):
        bag = BagTiles()
        taken = bag.take(7) # Take 7 to avoid the raise
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

    def test_put_full(self):
        bag = BagTiles()
        bag.put([Tile('A', 1)])
        self.assertEqual(TOTAL_TILES,len(bag.tiles))

####################
#      Start       #
####################

if __name__ == '__main__':
    unittest.main()
