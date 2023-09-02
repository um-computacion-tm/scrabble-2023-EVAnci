def menu(type=''):
    if type == 'menu':
        print('''    Menu
1) Ver tablero
2) Ver Atril
3) Ver Acciones
4) Ver Puntuaciones
Seleccion: ''')
    elif type == 'submenu':
        print('''|___  1) Introducir Palabra
|___  2) Cambiar Fichas
|___  3) Pasar Turno
|___  4) Rendirse
|___  5) Volver
Seleccion: ''')