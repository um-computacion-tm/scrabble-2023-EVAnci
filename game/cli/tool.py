class Tool():
    def menu(self,type=''):
        if type == 'menu':
            return('''    Menu
1) Ver tablero
2) Ver Atril
3) Ver Acciones
4) Ver Puntuaciones
    Seleccion: ''')
        elif type == 'submenu':
            return('''    |___  1) Introducir Palabra
    |___  2) Cambiar Fichas
    |___  3) Pasar Turno
    |___  4) Rendirse
    |___  5) Volver
    Seleccion: ''')

    def nav(self):
        selection = 'goback'
        while selection == 'goback':
            selection = self.range_input(1,4,self.menu('menu'))
            if selection == 1:
                selection = 'board'
            elif selection == 2:
                selection = 'lectern'
            elif selection == 3:
                selection = self.range_input(1,5,self.menu('submenu'))
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
    
    def input_int(self,message=''):
        try:
            selection = int(input(message))
            return selection
        except ValueError:
            print('Valor Invalido...')
            return 0 

    def range_input(self, from_value=0, to_value=0, message=''):
        selection = self.input_int(message)
        while not((from_value <= selection) and (selection <= to_value)):
            print(f'Debe ser un numero entre {from_value} y {to_value}')
            selection = self.input_int(message)
        return selection