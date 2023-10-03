# Battle ships
<hr>

Classic logic game, runs in Code Institute mock terminal on Heroku

User plays against the computer. The goal of the game is to find 
opponent's ships before he finds yours.

Each battleship placed in a single sector.

![Responsive](https://i.ibb.co/gr6JZ0Z/2023-10-02-21-21-34.png)
## How to play
<hr>

Based on classic game, where players try to find each other's
ships. Player who finds all the ships first wins the round.

The player can see his own ships and blank opponent's field.
The game has simple console design and uses basic characters 
to indicate game objects.

".."  - unknown sector

" > " - sector with a ship

" X " - sector with a sunk ship

" _ " - empty sector

## Features
<hr>

### Existing features
- Randomly generated fields for player and computer
- Computer's ships are concealed from the user

![battle field](https://i.ibb.co/3RxP0Qm/2023-10-02-22-06-13.png)

- Play against the computer
- Accepts user input
- Maintains scores and number of ships left
- Input validation - game accepts only valid coordinates
- Help messages at the top of the screen to inform user
about successful and unsuccessful turns, invalid inputs,
etc.
- If invalid coordinates entered - help message tells
user why his input failed validation.

![help message](https://i.ibb.co/sK9HSRk/2023-10-02-22-07-10.png)

- Data maintained in class instances
- Game screen refreshes each turn (program checks
computer's OS to pick the correct command)
- Rows are numbers and columns are letters (as in 
classic game).
- Player can quit the game at any time, entering "exit"
instead of coordinates
- Cheat mode. If user enters "mi6" instead of
coordinates - computer's ships become visible. This feature
was implemented for testing purpose

[Play here](https://tech-battle-ships-307012725313.herokuapp.com/)

![cheat mode](https://i.ibb.co/5kZhk1X/2023-10-02-22-07-25.png)

### Future features
- User can pick the number of ships and the field size
- User can choose difficulty: ( e.g. easy - if computer finds 
player's ship - it picks other coordinates, but just
ones; medium - the game as it is; hard - computer "knows"
location of one of the player's ships)
- Allow player place the ships himself
- Make ships of 1, 2 and 3 fields like in classic game

## Data model
<hr>
Class for the game fields, which stores player, number of
ships, their location, player's score and other additional
information.

Game creates two instances of this class for each player.
The class has methods for placing the ships, drawing the 
field, user input validation, player's and computer's
turns.

## Testing
<hr>
I have manually tested this project:

- Played the game myself
- Passed PEP8 linter to make sure that my code meets all
the requirements
- Given the game all types of invalid inputs
- Implement cheat mode to make testing faster ("mi6")

### Bugs
Working on my project I found several bugs caused by 
transforming data from stings to integers and back. I 
fixed it by checking the code step by step and using
print() function.

### Remaining bugs

- No bugs remaining

### Validator PEP8
- No errors were returned from pep8ci.herokuapp.com

## Deployments
<hr>
The project was deployed using Code Institute's mock
terminal for Heroku.
Steps for deployment:

- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in that order
- Link the Heroku app to the repository
- Click on "Deploy"

## Credits
<hr>

- Code Institute for the deployment terminal
- Code Institute for the idea and inspiration
of project interface
- Wikipedia for the details of the Battleships game
