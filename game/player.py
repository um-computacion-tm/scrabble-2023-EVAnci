from game.bagtiles import Wildcard

LECTERN_SIZE = 7

class Player:
    def __init__(self, name='', number=0, points=0):
        self.name = name
        self.number = number
        self.points = points
        self.times_pass = 0
        self.giveup = False
        self.lectern = []

    def give_tiles(self, tiles=[]):
        self.lectern.extend(tiles)

    def fill(self, bag_tiles):
        size = len(self.lectern) 
        self.give_tiles(bag_tiles.take(LECTERN_SIZE - size))

    def change_tiles(self, old_tiles_index=[], new_tiles=[]):
        old_tiles = []
        for i in range(len(old_tiles_index)):
            old_tiles.append(self.lectern[old_tiles_index[i]-1])
            self.lectern[old_tiles_index[i]-1] = new_tiles[i]
        return old_tiles

    def take(self, word):
        letters = self.split_word(word)
        return_tiles = []
        for letter in letters:
            for tile in self.lectern:
                if tile.letter == letter:
                    return_tiles.append(tile)
                    self.lectern.remove(tile)
                    break
                elif type(tile) == type(Wildcard()):
                    tile.letter = letter
                    return_tiles.append(tile)
                    self.lectern.remove(tile)
                    break
        return return_tiles

    def split_word(self,word):
        word = word.upper()
        if 'CH' in word:
            word = word.replace('CH','1')
        elif 'LL' in word:
            word =word.replace('LL','2')
        elif 'RR' in word:
            word = word.replace('RR', '3')
        result_word = []
        for letter in word:
            if letter == '1':
                result_word.append('CH')
            elif letter == '2':
                result_word.append('LL')
            elif letter == '3':
                result_word.append('RR')
            elif letter == 'Á':
                result_word.append('A')
            elif letter == 'É':
                result_word.append('E')
            elif letter == 'Í':
                result_word.append('I')
            elif letter == 'Ó':
                result_word.append('O')
            elif letter == 'Ú':
                result_word.append('U')    
            else:
                result_word.append(letter)
        return result_word

    def search(self, word):
        word = self.split_word(word)
        lectern = self.lectern.copy()
        valid = 0
        for letter in word:
            for tile in lectern:
                if letter == tile.letter or type(tile) == type(Wildcard()):
                    valid += 1
                    lectern.remove(tile)
                    break
        if valid == len(word):
            return True
        return False

    def __repr__(self):
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