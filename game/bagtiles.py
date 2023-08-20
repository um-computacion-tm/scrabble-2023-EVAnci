####################
#     Imports      #
####################

from os import path
import random, json

####################
#    Exceptions    #
####################

class PutBagFullException(Exception):
    pass

class TakeBagEmptyException(Exception):
    pass

####################
#     Constant     #
####################

TOTAL_TILES=100

# With the sentence 'with open() as name', the json file is open and 
# readed by python. To get the absolute directory where it's located
# I used path.abspath().
with open(path.abspath('tiles.json')) as json_file:
    DATA = json.load(json_file)
# The data collected in the json file is stored in the var 'data', 
# which then is used to store all the tiles in the 'tiles array'.

####################
#      Clases      #
####################

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class Wildcard(Tile):
    def __init__(self):
        super().__init__(letter='', value=0)

    def select_letter(self, selection):
        selection = selection.upper()
        for tile in DATA:
            if selection == tile['letter']:
                self.letter = tile['letter']
                self.value = tile['points']

class BagTiles:
    def __init__(self):
        self.tiles = []
        # Add the normal tiles to the bag
        for tile in DATA:
            for _ in range(tile['quantity']):
                self.tiles.append(Tile(tile['letter'], tile['points']))
        # Add the wildcard tiles to the bag
        for _ in range(2):
            self.tiles.append(Wildcard())
        # shuffle the bag
        random.shuffle(self.tiles)

    def take(self, count):
        tiles_taken = []
        try:
            if len(self.tiles) >= count:
                for _ in range(count):
                    tiles_taken.append(self.tiles.pop())
            else:
                raise TakeBagEmptyException
        except TakeBagEmptyException:
            pass
            # print('No hay suficientes fichas!') # Search how to notify the user in other way
        return tiles_taken

    def put(self, tiles):
        try:
            if len(self.tiles)+len(tiles) <= TOTAL_TILES:
                self.tiles.extend(tiles)
            else:
                raise PutBagFullException
        except PutBagFullException:
            pass
            # print('La bolsa esta llena o hay fichas de más!')