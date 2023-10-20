import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame, InvalidWord
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

    def test_player_points(self):
        scrabble = ScrabbleGame(players_count=2)
        scrabble.players[0].name = 'Hola'
        scrabble.players[1].name = 'Mundo'
        result = scrabble.player_points()
        expected = '''El jugador 1: (Hola) tiene 0 puntos
El jugador 2: (Mundo) tiene 0 puntos
'''
        self.assertEqual(result,expected)

    @patch('game.board.Board.validate')
    def test_play(self, mock_validate):
        mock_validate.return_value = True
        scrabble = ScrabbleGame(players_count = 3)
        scrabble.players[0].lectern = [Tile('C',1),Tile('A',1),Tile('S',3),Tile('A',1),Tile('L',2),Tile('R',3),Tile('C',1)]
        scrabble.next_turn()
        scrabble.play('casa',(7,7),True)
        self.assertEqual(scrabble.board.grid[7][7].tile.letter, 'C')
        self.assertEqual(scrabble.board.grid[7][8].tile.letter, 'A')
        self.assertEqual(scrabble.board.grid[7][9].tile.letter, 'S')
        self.assertEqual(scrabble.board.grid[7][10].tile.letter, 'A')

    @patch('game.board.Board.validate')
    def test_play_invalid_word(self, mock_validate):
        mock_validate.return_value = False
        scrabble = ScrabbleGame(players_count = 3)
        scrabble.players[0].lectern = [Tile('C',1),Tile('A',1),Tile('S',3),Tile('A',1),Tile('L',2),Tile('R',3),Tile('C',1)]
        scrabble.next_turn()
        with self.assertRaises(InvalidWord):
            scrabble.play('laa',(7,7),True)

    @patch('game.board.Board.validate')
    def test_play_almost_empty_bag(self, mock_validate):
        mock_validate.return_value = True
        scrabble = ScrabbleGame(players_count = 3)
        scrabble.players[0].lectern = [Tile('C',1),Tile('A',1),Tile('S',3),Tile('A',1),Tile('L',2),Tile('R',3),Tile('C',1)]
        scrabble.bag_tiles.take(76)
        scrabble.next_turn()
        scrabble.play('casa',(7,7),True)
        self.assertEqual(len(scrabble.players[0].lectern),6)

    @patch('game.board.Board.validate')
    def test_play_empty_bag(self, mock_validate):
        mock_validate.return_value = True
        scrabble = ScrabbleGame(players_count = 3)
        scrabble.players[0].lectern = [Tile('C',1),Tile('A',1),Tile('S',3),Tile('A',1),Tile('L',2),Tile('R',3),Tile('C',1)]
        scrabble.bag_tiles.take(79)
        scrabble.next_turn()
        scrabble.play('casa',(7,7),True)
        self.assertEqual(len(scrabble.players[0].lectern),3)

if __name__ == '__main__':
    unittest.main()