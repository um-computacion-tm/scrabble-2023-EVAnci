from os import path
import random, json

class InsufficientTiles(Exception):
    pass

class BagIsFull(Exception):
    pass

TOTAL_TILES=100

# With the sentence 'with open() as name', the json file is open and 
# readed by python. To get the absolute directory where it's located
# I used path.abspath().
# The data collected in the json file is stored in the var 'data', 
# which then is used to store all the tiles in the 'tiles array'.
with open(path.abspath('tiles.json')) as json_file:
    DATA = json.load(json_file)

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class Wildcard(Tile):
    def __init__(self):
        super().__init__(letter='?', value=0)

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

    def take(self, quantity):
        # 0 <= quantity <= 7
        tiles_taken = []
        if quantity == 0:
            return tiles_taken
        elif quantity <= len(self.tiles):
            for _ in range(quantity):
                tiles_taken.append(self.tiles.pop())
            return tiles_taken
        else:
            raise InsufficientTiles

    def put(self, tiles):
        if len(self.tiles)+len(tiles) <= TOTAL_TILES:
            self.tiles.extend(tiles)
        else:
            raise BagIsFull