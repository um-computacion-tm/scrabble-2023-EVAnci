# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Status: [Unreleased]

Development

## [0.3.0] - 2023-10-31

### Fixed

- Error while adding point to player in scrabble class.
    - The points where replaced with the points of the last word instead of being added.

### Known Issues

- A complex case with doble side validation isn't working.
- Wildcard Tile isn't supported yet

## [0.2.9] - 2023-10-30

### Fixed

- Board class:
    - Refactor validate not empty method.

- Fix an incorrect logical expresion in test.sh to start docker service if it's inactive.

### Known Issues

- A complex case with doble side validation isn't working.
- ~~Validate not empty method in board class has a cognitive complexity of 44, consider refactoring.~~
- ~~There is a complex logical expression in board class - Line 147~151.~~


## [0.2.8] - 2023-10-27

### Added

- Scrabble class:
    - Add end game coditions.
- Main class:
    - Add giveup and pass conditons

### Known Issues

- A complex case with doble side validation isn't working.
- Validate not empty method in board class has a cognitive complexity of 44, consider refactoring.
- There is a complex logical expression in board class - Line 147~151.

## [0.2.7] - 2023-10-26

### Added

- Main class:
    - Add missing tests to main class.

- Graph file that contains the output of lectern and board.

### Changed

- coveragerc file: ignore tests folder.
- Board class:
    - Refactor put word, to support intersections.
- test.sh
    - codeclimate engines:install was moved inside the if, as to not try to download codeclimate again once it's downloaded.

### Known Issues

- A complex case with doble side validation isn't working.
- Validate not empty method in board class has a cognitive complexity of 44, consider refactoring.
- There is a complex logical expression in board class - Line 147~151.

## [0.2.6] - 2023-10-25

### Fixed

- Refactor \_\_repr__ method in board class.

### Known Issues

- A complex case with doble side validation isn't working.
- Validate not empty method in board class has a cognitive complexity of 44, consider refactoring.
- There is a complex logical expression in board class - Line 147~151.

## [0.2.5] - 2023-10-24

### Fixed

- Refactor of calculate word value method to be less complex without losing functionality.

### Known Issues

- A complex case with doble side validation isn't working
- Validate not empty method in board class has a cognitive complexity of 44, consider refactoring.
- There is a complex logical expression in board class - Line 147~151.
- ~~Calculate word value method in board class is implemented but very complex. Consider refactoring.~~

## [0.2.4] - 2023-10-20

### Added

- Add tool class:
    - This class has the old validation isolated methods, menu and nav. They were moved to this class to improve modularity.
- Main class:
    - class constructor, game method and cli menu and navigation.

### Removed

- Cli Module:
    - Files that contain isolated methods (validate and menu) as long as they were migrated to new tools file. 

### Known Issues

- A complex case with doble side validation isn't working
- Calculate word value method in board class is implemented but very complex. Consider refactoring.

## [0.2.3] - 2023-10-19

### Changed

- Board class:
    - Improve calculate word value method to work with different cases of intersection of words.

### Known Issues

- A complex case with doble side validation isn't working

## [0.2.2] - 2023-10-18

### Changed

- Board class:
    - Refactor calculate word value method to calculate a word given a string instead of a list of cells

### Known Issues

- A complex case with doble side validation isn't working

## [0.2.1] - 2023-10-12

### Added

- Player class:
    - fill method, to fill the lectern with tiles of the bagtile

### Changed

- Player class:
    - refactor take tiles method, to take tiles from the lectern given a word instead of a list of letters.

### Known Issues

- A complex case with doble side validation isn't working

## [0.2.0] - 2023-10-09

### Added

- Tile class:
    - _\_repr__ method to print the letter of the tile.

- Cell class:
    - _\_repr__ method to print the letter of the tile in the cell.

- Board class:
    - Multipliers in the grid
    - Colors to grid multipliers

### Changed

- Board class:
    - Refactor _\_repr__ method to suppor double letter tiles and print cells with multipliers.

### Known Issues

- A complex case with doble side validation isn't working

## [0.1.9] - 2023-10-07

### Added

- Player class:
    - take method to take tiles from the lectern.

### Fixed

- Player class:
    - view_lectern method in player class has the \_\_repr__ mehtod to be printed.
    - Player class can handle words with accents.
        - The split_word method has been improved to support any type of input.

### Known Issues

- ~~The validation of words doesn't work with words with accents~~
- A complex case with doble side validation isn't working
- ~~view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod~~

## [0.1.8] - 2023-10-06

### Added

- Board class:
    - Add double intersection support in validation method.
    - Create a method rae_search to make methods less complex to understand.

### Changed

- Board class:
    - Horizontal validation and vertical validation fully working.
    - Refactor validate not empty method and submethods to be just one method.

### Removed

- Board class:
    - horizontal_validation and vertical_validation method as the code was practically duplicated.

### Fixed

- view method in board class rewritten as to be the \_\_repr__ mehtod

### Known Issues

- The validation of words doesn't work with words with accents
- ~~view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod~~
- A complex case with doble side validation isn't working
- view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod

## [0.1.7] - 2023-10-05

### Added

- Board class:
    - Complete horizontal_validate.
- Shell script to run codeclimate locally. 

### Changed

- Configuration of codeclimate to ignore cognitive-complexity analysis.

### Known Issues

- The validation of words doesn't work with words with accents
- view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod
- A complex case with doble side validation isn't working

## [0.1.6] - 2023-10-03 

### Added 

- Player class:
    - search method.
    - split_word method.
- Board class:
    - Complete vertical_validate.

### Fixed

- Search method in player class work to validate 'LL', 'RR' and 'CH'.

### Known Issues

- ~~Validation don't work for double letter tiles.~~
- The validation of words doesn't work with words with accents
- view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod

## [0.1.5] - 2023-10-01 

### Added 

- Refactor of validation methood in board class:
    - Divided the validation method.
    - Implemented validation to side words.

### Known Issues

- Validation don't work for double letter tiles.
- The validation of words doesn't work with words with accents
- view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod

### Fixed

- Conjugated verbs validation.

### Known Issues

- Validation don't work for double letter tiles.
- The validation of words doesn't work with words with accents
- view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod
- ~~Conjugated verbs had troubles in validation. Consider refactoring.~~

## [0.1.4] - 2023-09-29 

### Added 

- One dictionary file to validate words in case there is no internet connection.

### Known Issues

- Validation don't work for double letter tiles.
- The validation of words doesn't work with words with accents
- view method in board class and view_lectern method in player class should be rewritten as to be the \_\_repr__ mehtod

## [0.1.3] - 2023-09-28 

### Added

- Rasing exception for when the user is not connected to the internet in board class.

### Changed

- Mock the output of the dle.search_by_word for validate word method in board class.
- Raising exceptions when the bag is full and when are unsufficient tiles in the bag in bagtiles module.

### Removed

- Unnesessary comments in bagtiles module.

### Known Issues

- Validation don't work for double letter tiles.

## [0.1.2] - 2023-09-27 

### Added

- Add pyrae library to validate words in board class.

### Changed

- Remake validation testing in board class. 

### Known Issues

- Validation don't work for double letter tiles.

## [0.1.1] - 2023-09-12 

### Changed

- Upgrade validate_word method in board class to validate words that use other words or letters.

## [0.1.0] - 2023-09-08 

### Added

- Implemented tests for view_board and view_lectern methods.

### Fixed

- Moved _view_lectern_()  funtion to a player method.
- Moved _view_board_()  funtion to a board method.

## [0.0.9] - 2023-09-06 

### Added

- Add validate_word_inside_board method to the class board.
- Add next_turn method to scrabble class.

### Fixed

- Wildcard tile letter is '?', so print lectern works fine.

### Known Issues

- Some methods like print_board, print_lectern must be in the class it should be.
- main.py file is ignored by coverage, and is not tested by now

## [0.0.8] - 2023-09-03 

### Added

- Navigation system for the cli.
- Add give 7 tiles for each player.
- Show board and lectern function
- Add a line in .coveragerc file, to ignore main.py

### Changed

- Change menu print system to return the string.
- Modify some name in file cell.py 

### Removed

- Unnesessary print tests.

### Fixed

- Cli implementation is complete.

### Known Issues

- main.py file is ignored by coverage, and is not tested by now
- Wildcard tile hasn't a letter, print lectern get an error printing it

## [0.0.7] - 2023-09-02 

### Added

- end_game method in ScrabbleGame class.

### Changed

- Remake all cli file, making it more modular.

### Fixed

- All tests are complete and working.

### Known Issues

- Cli implementation is incomplete.

## [0.0.6] - 2023-09-01 

### Added

- Add cli file, with basic functionality.

### Known Issues

- Cli implementation is incomplete.
- Test cli isn't working.

## [0.0.5] - 2023-08-30 

### Added

- Add active attribute to cell class.
- Add calculate word value method to board class.
- Add circleci and codeclimate config files.

### Known Issues

- Anything at the moment.

## [0.0.4] - 2023-08-28 

### Added

- Game cell class with add letter and calculate value methods.
- Game 15x15 board.

### Fixed

- Add a missing if \_\_name__ == '\_\_main__' to test_player.py file.

## [0.0.3] - 2023-08-25 

### Added

- Player Class.
- Player methods to add and change tiles.
- requirements file.

### Known Issues

- Anything at the moment.

## [0.0.2] - 2023-08-20 

### Added
 
- Wildcard Tile class. 
- Wildcard Tile test.

### Changed 

- json file is saved in a global variable.

### Fixed

- Add the .coveragerc file that was ignored by git.

### Known Issues

- The full/empty bag message isn't properly implemented.

## [0.0.1] - 2023-08-17 

### Added 

- Exceptions to handle empty bag and full bag.
- Test for the exceptions.
- '_tiles.json_' file to store the tiles.
- Necesary code to use the json file in the program.

### Changed

- Upgrade take and put methods to raise and handle exceptions.
- Change some variable names to describe them better.
- Change module.py and test_module.py names to describe the file functionality.

### Removed

- The list of 98 tiles.

### Known Issues

- Anything at the moment.