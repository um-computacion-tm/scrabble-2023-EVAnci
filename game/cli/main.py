from game.scrabble import ScrabbleGame
from game.cli.tool import Tool

class Main():
    def __init__(self):
        self.tool = Tool()
        print('Bienvenido al juego Scrabble!')
        self.num_of_players = self.tool.range_input(
            from_value=2,
            to_value=4,
            message='Cantidad de jugadores [2,4]: '
            )
        self.scrabble = ScrabbleGame(self.num_of_players)
        for i in range(self.num_of_players):
            name = input(f'Nombre del jugador {self.scrabble.players[i].number}: ')
            self.scrabble.players[i].name = name
        self.scrabble.next_turn()
        self.round_number = 0

    def menu(self):
        selection = None
        while selection != 'pass' and selection != 'play' and selection != 'giveup':
            selection = self.tool.nav()
            if selection == 'board':
                print(self.scrabble.board)
            elif selection == 'lectern':
                print(self.scrabble.current_player)
            elif selection == 'points':
                print(self.scrabble.player_points())
            elif selection == 'play':
                selection = self.selection_play()
            elif selection == 'change':
                self.selection_change()
            elif selection == 'pass':
                pass
            elif selection == 'giveup':
                pass
            elif selection == 'goback':
                pass

    def selection_play(self):
        continue_game = False
        while not continue_game:
            word = input('Palabra: ')
            row = int(input('Posicion de la fila: '))
            column = int(input('Posicion de la columna: '))
            if input('Orientacion [H/V]: ').lower() == 'h':
                horizontal = True
            else:
                horizontal = False
            try:
                self.scrabble.play(word, (row,column), horizontal)
                continue_game = True
            except:
                retry = input('Esa palabra no es valida! Enter para intentalo otra vez o [M] para salir al menu.')
                if retry.upper() == 'M':
                    return None
        return 'play'
                
    def selection_change(self):
        print('Atril Actual:')
        print(self.scrabble.current_player)
        quantity = self.tool.range_input(0,7,'Cantidad de fichas a reemplazar [cancelar=0]: ')
        new_tiles = self.scrabble.bag_tiles.take(quantity)
        print('Seleccione el indice de las fichas a cambiar:')
        old_tiles_index = []
        for i in range(quantity):
            tile_index = self.tool.range_input(1,7,f'    > Indice de ficha N°{i+1}: ')
            old_tiles_index.append(tile_index)
        self.scrabble.bag_tiles.put(self.scrabble.current_player.change_tiles(old_tiles_index, new_tiles))
        print('Atril Resultante: ')
        print(self.scrabble.current_player)

    def game(self):
        while not(self.scrabble.end_game()):
            self.round_number += 1
            player = self.scrabble.current_player
            print(f'Ronda numero {self.round_number}')
            print(f'Fichas en bolsa: {len(self.scrabble.bag_tiles.tiles)}')
            print(f'Turno del jugador {player.number}: ({player.name})')
            self.menu()
            self.scrabble.next_turn()

if __name__ == '__main__':
    start = Main()
    start.game()