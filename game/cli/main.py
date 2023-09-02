from game.bagtiles import *
from game.board import * 
from game.cell import *
from game.player import *
from game.scrabble import * 
from game.cli.main import *
from game.cli.validate import *

print('Bienvenido al juego Scrabble!')
num_of_players = range_input(
    from_value=2,
    to_value=4,
    message='Cantidad de jugadores [2,4]: '
    )

scrabble = ScrabbleGame(num_of_players)

for i in range(num_of_players):
    name = input(f'Nombre del jugador {scrabble.players[i].number}:')
    scrabble.players[i].name = name

end_game = False

round_number = 0
while not(end_game):
    round_number += 1
    for turno in range(num_of_players):
        print(f'Turno del jugador {scrabble.players[turno].number} ({scrabble.players[turno].name})')
        selection = range_input(1,4,menu('menu'))
