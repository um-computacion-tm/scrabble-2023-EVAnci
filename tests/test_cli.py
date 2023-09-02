import unittest
from io import StringIO
from unittest.mock import patch
from game.cli.validate import *
from game.cli.menu import *

class TestCliValidate(unittest.TestCase):
    @patch('builtins.input', side_effect=[4])
    def test_input_int_valid(self, mock_input):
        value = input_int(message='Value: ')
        self.assertEqual(value, 4)

    @patch('builtins.input', side_effect=['a'])
    def test_input_int_invalid(self, mock_input):
        # Redirect stdout to StringIO object to capture the prints
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            value = input_int(message='Value: ')
        print_output = mock_stdout.getvalue()[:-1]
        self.assertEqual(value, 0)
        self.assertEqual(print_output, 'Valor Invalido...')

    @patch('builtins.input', side_effect=[1])
    def test_range_input_valid(self, mock_input):
        result = range_input(from_value=1, to_value=4, message="Ingrese un número entre 1 y 4: ")
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=[5, 2])
    def test_range_input_second_valid(self, mock_input):
        result = range_input(from_value=1, to_value=4, message="Ingrese un número entre 1 y 4: ")
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['a', 6, 3])
    def test_range_input_invalid(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            value = range_input(from_value=1, to_value=4, message="Ingrese un número entre 1 y 4: ")
        self.assertEqual(value, 3)

class TestCliMenu(unittest.TestCase):
    def test_menu_print(self):
        print_output = menu(type='menu')
        self.assertEqual(
            print_output,
            '''    Menu
1) Ver tablero
2) Ver Atril
3) Ver Acciones
4) Ver Puntuaciones
Seleccion: '''
        )

    def test_submenu_print(self):
        print_output = menu(type='submenu')
        self.assertEqual(
            print_output,
            '''|___  1) Introducir Palabra
|___  2) Cambiar Fichas
|___  3) Pasar Turno
|___  4) Rendirse
|___  5) Volver
Seleccion: '''
        )

    @patch('builtins.input', side_effect=[1])
    def test_menu_nav1(self, mock_input):
        result = nav()
        self.assertEqual(result, 'board')

    @patch('builtins.input', side_effect=[2])
    def test_menu_nav2(self, mock_input):
        result = nav()
        self.assertEqual(result, 'lectern')

    @patch('builtins.input', side_effect=[3,1])
    def test_menu_nav31(self, mock_input):
        result = nav()
        self.assertEqual(result, 'play')

    @patch('builtins.input', side_effect=[3,2])
    def test_menu_nav32(self, mock_input):
        result = nav()
        self.assertEqual(result, 'change')

    @patch('builtins.input', side_effect=[3,3])
    def test_menu_nav33(self, mock_input):
        result = nav()
        self.assertEqual(result, 'pass')

    @patch('builtins.input', side_effect=[3,4])
    def test_menu_nav34(self, mock_input):
        result = nav()
        self.assertEqual(result, 'giveup')

    @patch('builtins.input', side_effect=[3,5,1])
    def test_menu_nav35(self, mock_input):
        result = nav()
        self.assertEqual(result, 'board')

    @patch('builtins.input', side_effect=[4])
    def test_menu_nav4(self, mock_input):
        result = nav()
        self.assertEqual(result, 'points')

if __name__ == '__main__':
    unittest.main()