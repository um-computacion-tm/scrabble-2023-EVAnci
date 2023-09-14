LECTERN_SIZE = 7

class Player:
    def __init__(self, name='', number=0, points=0):
        self.name = name
        self.number = number
        self.points = points
        self.lectern = []

    def give_tiles(self, tiles=[]):
        self.lectern.extend(tiles)

    def change_tiles(self, old_tiles_index=[], new_tiles=[]):
        old_tiles = []
        for i in range(len(old_tiles_index)):
            old_tiles.append(self.lectern[old_tiles_index[i]-1])
            self.lectern[old_tiles_index[i]-1] = new_tiles[i]
        return old_tiles

    def view_lectern(self):
        view = '                     ATRIL\n\n'
        view += f'Letras -> '
        letters = ''
        letters_index = ''
        for i in range(len(self.lectern)):
            letters += f' | {self.lectern[i].letter}'
            if len(self.lectern[i].letter) == 1:
                letters_index += f'   {i+1}'
            else:
                letters_index += f'    {i+1}'
        letters += f' |'
        view += letters+'\n'
        view += f'Indice -> '
        view += letters_index+'\n\n'
        return view