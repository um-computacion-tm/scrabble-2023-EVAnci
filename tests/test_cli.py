import unittest
from unittest.mock import patch

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=[])
    def test_player_quantity_input(self, mock_input):
        pass

if __name__ == '__main__':
    unittest.main()