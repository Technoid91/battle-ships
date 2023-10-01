import os
import platform
from random import randint

user_name = ''
class GameField():

    def __init__(self, player, ships):
        """
        Initiation method of the class
        """
        self.player = player
        self.ships = ships
        self.field = []
        self.score = 0
        self.message = ''

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

    def get_message(self):
        """
        Returns help message for player depending on his actions
        """
        return self.message

    def draw_field(self):
        """
        Draws game field on the screen
        """

        print('-' * 40)
        if self.player == 'player':
            print(user_name + "'s field")
        else:
            print("Computer's field")
        print('    A  B  C  D  E')
        row_num = 1

        for row in self.field:
            row_2_draw = str(row_num) + ' '
            for element in row:
                # hides computer's ships from the player
                if self.player != 'player' and element == ' >':
                    element = ' .. '
                row_2_draw = row_2_draw + element
            print(row_2_draw)
            row_num += 1


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


def clear_screen():
    """
    Wipes the console screen to refresh output information
    on Windows, Linux and macOS.
    Does not work on other (rare) operating systems
    """
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('clr')
    elif os_name == 'Linux' or 'Darvin':
        os.system('clear')
    else:
        pass


def game_interface(game_info):
    '''
    Shows informative game interface at the top of the screen.
    3 arguments are required: help message, amount of user's
    ships left, amount of computer_ships
    '''
    user_ships = game_info[0]
    computer_ships = game_info[1]
    message = game_info[2]
    print('------------BATTLE SHIPS------------')
    print(f'Your ships: {user_ships}  |  Computer ships: {computer_ships}')
    print('-'*40)
    if message:
        print(message)
    else:
        print('\n')


def game_round(player, computer):
    """
    Draws game field and ask user to pick coordinates
    """
    player.draw_field()
    computer.draw_field()
    print('-'*40)
    print('Pick coordinates to strike, e.g. B5\n(enter "exit" to quit)')
    print('-'*40)
    user_shoot = input('Enter here: ')



def main():
    """
    Executes the main game code
    """
    clear_screen()
    initial_screen()

    player_field = GameField('player', 4)
    computer_field = GameField('computer', 4)
    player_field.place_ships()
    computer_field.place_ships()

    while True:
        clear_screen()
        user_ships = player_field.ships_left()
        computer_ships = computer_field.ships_left()
        if user_ships == 0 or computer_ships == 0:
            break
        help_message = computer_field.get_message()
        game_info = [user_ships, computer_ships, help_message]
        game_interface(game_info)

        game_round(player_field, computer_field)

main()
