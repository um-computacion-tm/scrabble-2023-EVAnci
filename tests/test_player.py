import unittest
from game.player import Player, LECTERN_SIZE
from game.bagtiles import BagTiles, Tile
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

    def test_split_word(self):
        player = Player()
        splited_word = player.split_word('CASA')
        self.assertEqual(splited_word, ['C','A','S','A'])

    def test_split_word_with_ll(self):
        player = Player()
        splited_word = player.split_word('llano')
        self.assertEqual(splited_word, ['LL','A','N','O'])

    def test_split_word_with_ch(self):
        player = Player()
        splited_word = player.split_word('chamba')
        self.assertEqual(splited_word, ['CH','A','M','B','A'])

    def test_split_word_with_rr(self):
        player = Player()
        splited_word = player.split_word('ferro')
        self.assertEqual(splited_word, ['F','E','RR','O'])

    def test_search_word(self):
        player = Player()
        player.give_tiles([Tile('A',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('S',3), Tile('G',2)])
        result = player.search('casa')
        self.assertEqual(result, True)

    def test_search_word_invalid(self):
        player = Player()
        player.give_tiles([Tile('A',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('S',3), Tile('G',2)])
        result = player.search('losa')
        self.assertEqual(result, False)

    def test_search_word_2_same_letter(self):
        player = Player()
        player.give_tiles([Tile('Y',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('G',3), Tile('G',2)])
        result = player.search('casas')
        self.assertEqual(result, False)

    def test_search_double_letter_tile_word(self):
        player = Player()
        player.give_tiles([Tile('LL',1), Tile('U', 1), Tile('V',1), Tile('I',3), Tile('A',1), Tile('G',3), Tile('G',2)])
        result = player.search('lluvia')
        self.assertEqual(result, True)

    def test_print_lectern(self):
        player = Player()
        tiles = []
        for i in range(6):
            tiles.append(Tile('A',1))
        tiles.append(Tile('AA',1))
        player.give_tiles(tiles)
        actual_output = player.view_lectern()
        expected_output = '''                     ATRIL

Letras ->  | A | A | A | A | A | A | AA |
Indice ->    1   2   3   4   5   6    7

'''
        self.assertEqual(actual_output,expected_output)


if __name__ == '__main__':
    unittest.main()