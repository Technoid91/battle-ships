import os
import platform
from random import randint

class GameField():

    def __init__(self, player, ships):
        """
        Initiation method of the class
        """
        self.player = player
        self.ships = ships
        self.field = []
        self.score = 0

    def place_ships(self):
        """
        Randomly places the ships on the game's field
        """
        #the row without ships
        skip_row = randint(0, self.ships)
        ships = self.ships
        row = 0
        while row < ships + 1:
            row_list = [' .. ', ' .. ', ' .. ', ' .. ', ' .. ']
            if row == skip_row:
                self.field.append(row_list)
            else:
                column = randint(0, 4)
                # ' >' - the ship symbol
                row_list[column] = ' >'
                self.field.append(row_list)
            row += 1

    def ships_left(self):
        """
        Returns amount of the ships left
        """
        return self.ships


def initial_screen():
    """
    First screen user sees. It asks user is he wants to start the game
    and his name
    """
    print('-'*40)
    print('Welcome to BATTLE SHIPS')
    print('Board size: 5. Number of ships: 4')
    print('-'*40)
    s = None
    while s != 'y':
        s = input('To start the game enter "y": ')
        s = s.lower() # in case if Caps lock is active
        print('user input: '+s)
    print('-'*40)
    global user_name
    while not user_name:
        user_name = input('Please enter your name: ')
        user_name = user_name[:10]
def main():
    """
    Executes the main game code
    """

    initial_screen()

    player_field = GameField('player', 4)
    computer_field = GameField('computer', 4)
    player_field.place_ships()
    computer_field.place_ships()

    while True:
        user_ships = player_field.ships_left()
        computer_ships = computer_field.ships_left()
        if user_ships == 0 or computer_ships == 0:
            break

main()
