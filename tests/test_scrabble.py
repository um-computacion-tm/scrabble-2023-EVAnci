import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_end_game_false(self):
        scrabble_game = ScrabbleGame(players_count=3)
        end_game = scrabble_game.end_game()
        self.assertEqual(end_game,False)

    def test_end_game_true(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles.take(100)
        end_game = scrabble_game.end_game()
        self.assertEqual(end_game,True)

if __name__ == '__main__':
    unittest.main()
