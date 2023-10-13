import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.bagtiles import Tile

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
        scrabble_game = ScrabbleGame(players_count=0)
        scrabble_game.bag_tiles.take(100)
        end_game = scrabble_game.end_game()
        self.assertEqual(end_game,True)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    @patch('game.board.Board.validate')
    def test_play(self, mock_validate):
        mock_validate.return_value = True
        scrabble = ScrabbleGame(players_count = 3)
        scrabble.players[0].lectern = [Tile('C',1),Tile('A',1),Tile('S',3),Tile('A',1),Tile('L',2),Tile('R',3),Tile('C',1)]
        scrabble.play('casa',(7,7),True,scrabble.players[0])
        self.assertEqual(scrabble.board.grid[7][7].tile.letter, 'C')
        self.assertEqual(scrabble.board.grid[7][8].tile.letter, 'A')
        self.assertEqual(scrabble.board.grid[7][9].tile.letter, 'S')
        self.assertEqual(scrabble.board.grid[7][10].tile.letter, 'A')

if __name__ == '__main__':
    unittest.main()