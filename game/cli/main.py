from game.scrabble import ScrabbleGame
from game.cli.tool import Tool
import random

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
        while selection != 'pass' and selection != 'giveup':
            selection = self.tool.nav()
            if selection == 'board':
                print(self.scrabble.board)
            elif selection == 'lectern':
                print(self.scrabble.current_player)
            elif selection == 'points':
                print(self.scrabble.player_points())
            elif selection == 'play':
                selection = self.selection_play()
                self.scrabble.current_player.times_pass = 0
            elif selection == 'change':
                selection = self.selection_change()
            elif selection == 'pass':
                self.scrabble.current_player.times_pass += 1
            elif selection == 'giveup':
                self.scrabble.current_player.giveup = True
            elif selection == 'goback':
                pass

    def selection_play(self):
        continue_game = False
        while not continue_game:
            word = input('Palabra: ')
            row = self.tool.range_input(1,15,'Posicion de la fila: ')-1
            column = self.tool.range_input(1,15,'Posicion de la columna: ')-1
            horizontal = True if input('Orientacion [H/V]: ').lower() == 'h'else False
            try:
                self.scrabble.play(word, (row,column), horizontal)
                continue_game = True
            except:
                print('Esa palabra no es valida! Revisa tu conexion a internet si crees que tu palabra es valida.')
                retry = input('Enter para intentalo otra vez o [M] para salir al menu.')
                if retry.upper() == 'M':
                    return None
        return 'pass'
                
    def selection_change(self):
        print('Atril Actual:')
        print(self.scrabble.current_player)
        quantity = self.tool.range_input(0,7,'Cantidad de fichas a reemplazar [cancelar=0]: ')
        new_tiles = self.scrabble.bag_tiles.take(quantity)
        if quantity > 0:
            print('Seleccione el indice de las fichas a cambiar:'if quantity < 7 else 'Cambiando todas las fichas...')
        else:
            return None
        old_tiles_index = []
        for i in range(quantity):
            tile_index = self.tool.range_input(1,7,f'    > Indice de ficha N°{i+1}: ') if quantity < 7 else i
            old_tiles_index.append(tile_index)
        self.scrabble.bag_tiles.put(self.scrabble.current_player.change_tiles(old_tiles_index, new_tiles))
        random.shuffle(self.scrabble.bag_tiles.tiles)
        print('Atril Resultante: ')
        print(self.scrabble.current_player)
        return 'pass'
    
    def end(self):
        winners_result = self.scrabble.winners()
        print('Los ganadores son: ')
        for i, player in enumerate(winners_result):
            print(f'{i}. Jugador: {player.name} - Puntaje: {player.points}')

    def game(self):
        while not(self.scrabble.end_game()):
            self.round_number += 1
            player = self.scrabble.current_player
            print(f'Ronda numero {self.round_number}')
            print(f'Fichas en bolsa: {len(self.scrabble.bag_tiles.tiles)}')
            print(f'Turno del jugador {player.number}: ({player.name})')
            self.menu()
            self.scrabble.next_turn()
        self.end()

if __name__ == '__main__':
    start = Main()
    start.game()