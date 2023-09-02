from game.cli.validate import *

def menu(type=''):
    if type == 'menu':
        return('''    Menu
1) Ver tablero
2) Ver Atril
3) Ver Acciones
4) Ver Puntuaciones
Seleccion: ''')
    elif type == 'submenu':
        return('''|___  1) Introducir Palabra
|___  2) Cambiar Fichas
|___  3) Pasar Turno
|___  4) Rendirse
|___  5) Volver
Seleccion: ''')

def nav():
    selection = 'goback'
    while selection == 'goback':
        selection = range_input(1,4,menu('menu'))
        if selection == 1:
            selection = 'board'
        elif selection == 2:
            selection = 'lectern'
        elif selection == 3:
            selection = range_input(1,5,menu('submenu'))
            if selection == 1:
                selection = 'play'
            elif selection == 2:
                selection = 'change'
            elif selection == 3:
                selection = 'pass'
            elif selection == 4:
                selection = 'giveup'
            elif selection == 5:
                selection = 'goback'
        elif selection == 4:
            selection = 'points'
    return selection