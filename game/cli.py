def menu():
    print('''1) Ver tablero
    2) Ver Atril
    3) Ver Acciones
    4) Ver Puntuaciones
    ''')

while True:
    try:
        num_of_players = int(input('Cantidad de jugadores: '))
        if 2 <= num_of_players and num_of_players <= 4:
            break
        else:
            raise ValueError
    except ValueError:
        print('Debe ser un numero entero entre 2 y 4')

end_game = False

round_number = 0
while not(end_game):
    round_number += 1
    for turno in range(num_of_players):
        print(f'Turno del jugador {turno+1}')