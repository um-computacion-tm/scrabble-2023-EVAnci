import unittest
from game.player import Player, LECTERN_SIZE
from unittest.mock import patch

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player('Isaac', 1, 3)
        self.assertEqual(player.name, 'Isaac')
        self.assertEqual(player.number, 1)
        self.assertEqual(player.points, 3)
        self.assertEqual(player.lectern, [])
