from game.scrabble import * 
from game.cli.menu import *
from game.cli.validate import *

print('Bienvenido al juego Scrabble!')
num_of_players = range_input(
    from_value=2,
    to_value=4,
    message='Cantidad de jugadores [2,4]: '
    )

scrabble = ScrabbleGame(num_of_players)

for i in range(num_of_players):
    name = input(f'Nombre del jugador {scrabble.players[i].number}: ')
    scrabble.players[i].name = name

end_game = False

round_number = 0
while not(end_game):
    round_number += 1
    print(f'Ronda numero {round_number}')
    for turno in range(num_of_players):
        selection = None
        while selection != 'pass' and selection != 'play' and selection != 'giveup':
            print(f'Turno del jugador {scrabble.players[turno].number} ({scrabble.players[turno].name})  ')
            selection = nav()
            if selection == 'board':
                print(scrabble.board.view())
            elif selection == 'lectern':
                print(scrabble.players[turno].view_lectern())
            elif selection == 'points':
                for i in range(num_of_players):
                    print(f'El jugador {scrabble.players[i].number} ({scrabble.players[i].name}) tiene {scrabble.players[i].points} puntos')
            elif selection == 'play':
                pass
            elif selection == 'change':
                print('Atril Actual:')
                print_lectern(scrabble.players[turno].lectern)
                quantity = range_input(0,7,'Numero de fichas a reemplazar [cancelar=0]: ')
                new_tiles = scrabble.bag_tiles.take(quantity)
                print('Seleccione el indice de las fichas a cambiar:')
                old_tiles_index = []
                for i in range(quantity):
                    tile_index = range_input(1,7,f'   {i+1}) Indice de ficha: ')
                    old_tiles_index.append(tile_index)
                scrabble.bag_tiles.put(scrabble.players[turno].change_tiles(old_tiles_index, new_tiles))
                print('Atril Resultante: ')
                print_lectern(scrabble.players[turno].lectern)
            elif selection == 'pass':
                pass
            elif selection == 'giveup':
                end_game = True
            elif selection == 'goback':
                pass