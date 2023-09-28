# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Status

Development

## [0.0.13] - 2023-09-28 (development)

### Added

- Rasing exception for when the user is not connected to the internet in board class.

### Changed

- Mock the output of the dle.search_by_word for validate word method in board class.
- Raising exceptions when the bag is full and when are unsufficient tiles in the bag in bagtiles module.

### Removed

- Unnesessary comments in bagtiles module.

### Known Issues

- Validation don't work for double letter tiles.

## [0.0.12] - 2023-09-27 (development)

### Added

- Add pyrae library to validate words in board class.

### Changed

- Remake validation testing in board class. 

### Known Issues

- Validation don't work for double letter tiles.

## [0.0.11] - 2023-09-12 (development)

### Changed

- Upgrade validate_word method in board class to validate words that use other words or letters.

## [0.0.10] - 2023-09-08 (development)

### Added

- Implemented tests for view_board and view_lectern methods.

### Fixed

- Moved _view_lectern_()  funtion to a player method.
- Moved _view_board_()  funtion to a board method.

## [0.0.9] - 2023-09-06 (development)

### Added

- Add validate_word_inside_board method to the class board.
- Add next_turn method to scrabble class.

### Fixed

- Wildcard tile letter is '?', so print lectern works fine.

### Known Issues

- Some methods like print_board, print_lectern must be in the class it should be.
- main.py file is ignored by coverage, and is not tested by now

## [0.0.8] - 2023-09-03 (development)

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

## [0.0.7] - 2023-09-02 (development)

### Added

- end_game method in ScrabbleGame class.

### Changed

- Remake all cli file, making it more modular.

### Fixed

- All tests are complete and working.

### Known Issues

- Cli implementation is incomplete.

## [0.0.6] - 2023-09-01 (development)

### Added

- Add cli file, with basic functionality.

### Known Issues

- Cli implementation is incomplete.
- Test cli isn't working.

## [0.0.5] - 2023-08-30 (development)

### Added

- Add active attribute to cell class.
- Add calculate word value method to board class.
- Add circleci and codeclimate config files.

### Known Issues

- Anything at the moment.

## [0.0.4] - 2023-08-28 (development)

### Added

- Game cell class with add letter and calculate value methods.
- Game 15x15 board.

### Fixed

- Add a missing if \_\_name__ == '\_\_main__' to test_player.py file.

## [0.0.3] - 2023-08-25 (development)

### Added

- Player Class.
- Player methods to add and change tiles.
- requirements file.

### Known Issues

- Anything at the moment.

## [0.0.2] - 2023-08-20 (development)

### Added
 
- Wildcard Tile class. 
- Wildcard Tile test.

### Changed 

- json file is saved in a global variable.

### Fixed

- Add the .coveragerc file that was ignored by git.

### Known Issues

- The full/empty bag message isn't properly implemented.

## [0.0.1] - 2023-08-17 (development)

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

### Knowm Issues

- Anything at the moment.