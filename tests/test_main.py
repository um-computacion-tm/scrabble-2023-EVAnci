import unittest, io, sys
from unittest.mock import patch, Mock
from game.cli.main import Main
from game.bagtiles import Tile
from tests.graph import BOARD_OUTPUT, LECTERN_OUTPUT

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    def test_main_init(self, mock_input, mock_range_input):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        sys.stdout = sys.__stdout__
        self.assertNotEqual(main.tool, None)
        self.assertNotEqual(main.scrabble, None)
        self.assertEqual(len(main.scrabble.players),2)
        self.assertNotEqual(main.scrabble.current_player, None)
        self.assertEqual(main.round_number,0)

    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    @patch('game.cli.main.Tool.nav', side_effect=['board','pass'])
    def test_main_menu_board(self, mock_input, mock_range_input, mock_nav):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        # Reset buffer, to erase main output
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        expected = BOARD_OUTPUT+'\n'
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    @patch('game.cli.main.Tool.nav', side_effect=['lectern','pass'])
    def test_main_menu_lectern(self, mock_input, mock_range_input, mock_nav):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        main.scrabble.players[0].lectern = [Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('A',1),Tile('AA',1)]
        # Reset buffer, to erase main output
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        expected = LECTERN_OUTPUT+'\n'
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    @patch('game.cli.main.Tool.nav', side_effect=['points','pass'])
    def test_main_menu_points(self, mock_input, mock_range_input, mock_nav):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        # Reset buffer, to erase main output
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        expected = 'El jugador 1: (elio) tiene 0 puntos\nEl jugador 2: (valen) tiene 0 puntos\n\n'
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    @patch('game.cli.main.Tool.nav', side_effect=['play','pass'])
    def test_main_menu_play(self, mock_input, mock_range_input, mock_nav):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        with patch.object(main, 'selection_play') as mock_play:
            main.menu()
            mock_play.assert_called_once()
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=['elio','valen'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    @patch('game.cli.main.Tool.nav', side_effect=['change','pass'])
    def test_main_menu_change(self, mock_input, mock_range_input, mock_nav):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        with patch.object(main, 'selection_change') as mock_change:
            main.menu()
            mock_change.assert_called_once()
        sys.stdout = sys.__stdout__
    
    @patch('builtins.input', side_effect=['elio','valen','palabra',7,7,'H'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    def test_selection_play(self, mock_input, mock_range_input):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        mock_play = Mock()
        main.scrabble.play = mock_play
        main.selection_play()
        sys.stdout = sys.__stdout__
        mock_play.assert_called_once()

    @patch('builtins.input', side_effect=['elio','valen','palabra',7,7,'H','M'])
    @patch('game.cli.main.Tool.range_input', return_value=2)
    def test_selection_play_exception(self, mock_input, mock_range_input):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        mock_play = Mock()
        mock_play.side_effect = Exception()
        main.scrabble.play = mock_play
        return_value = main.selection_play()
        sys.stdout = sys.__stdout__
        self.assertEqual(return_value, None)

if __name__ == '__main__':
    unittest.main()