import unittest
from game.player import Player, LECTERN_SIZE
from game.bagtiles import BagTiles
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player(name='Isaac', number=1, points=3)
        self.assertEqual(player.name, 'Isaac')
        self.assertEqual(player.number, 1)
        self.assertEqual(player.points, 3)
        self.assertEqual(player.lectern, [])

    def test_player_creation_no_parameters(self):
        player = Player()
        self.assertEqual(player.name, '')
        self.assertEqual(player.number, 0)
        self.assertEqual(player.points, 0)
        self.assertEqual(player.lectern, [])

    def test_give_tiles(self):
        player = Player()
        player.give_tiles(['A', 'B'])
        self.assertEqual(player.lectern, ['A', 'B'])

    def test_give_tiles_from_bag(self):
        bag = BagTiles()
        player = Player()
        player.give_tiles(bag.take(7))
        self.assertEqual(len(player.lectern), 7)

    def test_change_tiles(self):
        player = Player()
        player.give_tiles(['A', 'B', 'C'])
        old_tiles = player.change_tiles(old_tiles_index=[2,3], new_tiles=['Z', 'Y'])
        self.assertEqual(player.lectern, ['A', 'Z', 'Y'])
        self.assertEqual(old_tiles, ['B', 'C'])

if __name__ == '__main__':
    unittest.main()