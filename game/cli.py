main_menu = '''    Menu
1) Ver tablero
2) Ver Atril
3) Ver Acciones
4) Ver Puntuaciones
'''

sub_menu = '''|___  1) Introducir Palabra
|___  2) Cambiar Fichas
|___  3) Pasar Turno
|___  4) Rendirse
'''

def validate_input(first_value=0,last_value=0,input_message='', error_message=''):
    while True:
        try:
            selection = int(input(input_message))
            if selection >= first_value and selection <= last_value:
                return selection
                break
            else:
                raise ValueError
        except ValueError:
            print(error_message)

def menu():
    print(main_menu)
    selection = validate_input(
        1,
        4,
        'Selection -> ', 
        'Valor Invalido...'
        )
    if selection == 3:
        print(sub_menu)



num_of_players = None
while num_of_players==None:
    num_of_players = validate_input(
        1,
        4,
        'Cantidad de jugadores: ',
        'Debe ser un numero entero entre 2 y 4'
        )

end_game = False

round_number = 0
while not(end_game):
    round_number += 1
    for turno in range(num_of_players):
        print(f'Turno del jugador {turno+1}')
        menu()