# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Status

Development

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