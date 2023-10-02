import os
import platform
from random import randint

user_name = ''


class GameField:

    def __init__(self, player, ships):
        """
        Initiation method of the class
        """
        self.player = player
        self.ships = ships
        self.field = []
        self.score = 0
        self.message = ''
        self.coordinates = ''
        self.show_ships = False

    def place_ships(self):
        """
        Randomly places the ships on the game's field
        """
        # the row without ships
        skip_row = randint(0, self.ships)
        ships = self.ships
        row = 0
        while row < ships + 1:
            row_list = [' .. ', ' .. ', ' .. ', ' .. ', ' .. ']
            if row == skip_row:
                self.field.append(row_list)
            else:
                column = randint(0, 4)
                # ' > ' - the ship symbol
                row_list[column] = ' > '
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

        print('-' * 35)
        if self.player == 'player':
            print(user_name + "'s field")
        else:
            print("Computer's field")
        print('   A    B    C    D    E')
        row_num = 1

        for row in self.field:
            row_2_draw = str(row_num) + ' '
            for element in row:
                # hides computer's ships from the player
                if self.player != 'player' and element == ' > ':
                    # if cheat mode disabled
                    if not self.show_ships:
                        element = ' .. '
                row_2_draw = row_2_draw + element
            print(row_2_draw)
            row_num += 1

    def validation(self, coordinates):
        """
        Checks if the user's coordinates are correct
        """

        self.coordinates = coordinates
        columns = ['A', 'B', 'C', 'D', 'E']
        rows = ['1', '2', '3', '4', '5']
        # Checks if it's just two characters
        if len(coordinates) == 2:
            column = coordinates[:-1].upper()
            row = coordinates[1:]
            # Checks if coordinates are in valid range
            if column in columns:
                y = columns.index(column)
            # Checks if coordinates are specified in the correct order
            elif column in rows:
                self.message = 'Wrong value\nLetter then figure. For example: B2'
                return False
            else:
                self.message = 'Wrong value\nLetter must be from A to E'
                return False
            if row in rows:
                x = rows.index(row)
            else:
                self.message = 'Please enter letter then figure.\nFigure must be from 1 to 5'
                return False
            # Checks if user picked the same coordinates as before
            if self.field[x][y] == '  _ ' or self.field[x][y] == ' X ':
                self.message = 'This sector is already clear.\nPick another one'
                return False
            self.coordinates = str(y) + str(x)
            return True
        else:
            self.message = 'Only letter and figure.\nFor example: B2'
            return False

    def shoot(self):
        """
        Transforms user's coordinates and informs if he missed or not.
        Also makes computer's move
        """
        # User's shoot
        if self.player == 'computer':
            coordinates = self.coordinates
            x = int(coordinates[1:])  # rows
            y = int(coordinates[:-1])  # columns
            field_point = self.field[x][y]
        else:
            # Computer's shoot
            while True:
                x = randint(0, 4)
                y = randint(0, 4)
                field_point = self.field[x][y]
                # Avoids repetitions in shoots
                if field_point == ' .. ' or field_point == ' >':
                    break
        if field_point == ' > ':
            self.ships -= 1
            self.field[x][y] = ' X '  # drowned ship
            self.message = '\n\tNICE SHOT!' if self.player == 'computer' else ' '
            self.score += 1
        else:
            self.message = '\n\t       missed' if self.player == 'computer' else ' '
            self.field[x][y] = '  _ '  # missed target

    def stat(self):
        """
        Returns the score based on how many
        enemy's ships destroyed
        """
        return self.score

    def give_up(self):
        """
        Makes amount of ships 0
        """
        self.ships = 0

    def cheat(self):
        """
        Reveals computer's ships on the field.
        Secret cheating function, very handy for testing
        (makes game extremely boring)
        """
        if self.show_ships:
            self.show_ships = False
            self.message = '\n--> CHEAT DISABLED! <--'
        else:
            self.show_ships = True
            self.message = '\n--> CHEAT ENABLED! <--'


def initial_screen():
    """
    First screen user sees. It asks user is he wants to start the game
    and his name
    """
    print('-' * 35)
    print('Welcome to BATTLE SHIPS')
    print('Board size: 5. Number of ships: 4')
    print('-' * 35)
    s = None
    while s != 'y':
        s = input('To start the game enter "y": \n')
        s = s.lower()  # in case if Caps lock is active
        print('user input: ' + s)
    print('-' * 35)
    global user_name
    while not user_name:
        user_name = input('Please enter your name: \n')
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
        return


def game_interface(game_info):
    """
    Shows informative game interface at the top of the screen.
    3 arguments are required: help message, amount of user's
    ships left, amount of computer_ships
    """
    user_ships = game_info[0]
    computer_ships = game_info[1]
    message = game_info[2]
    print('------------BATTLE SHIPS------------')
    print(f'Your ships: {user_ships}  |  Computer ships: {computer_ships}')
    print('-' * 35)
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
    print('-' * 35)
    print('Pick coordinates to strike, e.g. B5\n(enter "exit" to quit)')
    print('-' * 35)
    user_shoot = input('Enter here: \n')
    # Exiting the game
    if user_shoot == 'exit':
        computer.give_up()
        player.give_up()
        return
    # Cheat to reveal computer's ships
    elif user_shoot == 'mi6':
        computer.cheat()
        return
    correct_shoot = computer.validation(user_shoot)
    if correct_shoot:
        computer.shoot()
        player.shoot()


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
        # Game ends when one of the players is out of ships
        if user_ships == 0 or computer_ships == 0:
            break
        help_message = computer_field.get_message()
        game_info = [user_ships, computer_ships, help_message]
        game_interface(game_info)

        game_round(player_field, computer_field)

    # End of the game
    clear_screen()
    # Exit before game is finished
    if user_ships + computer_ships == 0:
        print(f'Bye, {user_name}...')
        return

    print('\n\n' + '*' * 30)

    player_score = computer_field.stat()
    computer_score = player_field.stat()
    # User wins
    if user_ships > computer_ships:
        print('\tCONGRATULATIONS!')
        print('*' * 35)
        print(f'\t{user_name} WINS!')
    # User loses
    else:
        print(f'\tSorry, {user_name}')
        print('*' * 35)
        print("Your fleet was destroyed")
    print(f'SCORE:  {player_score}:{computer_score}')
    print('*' * 35)
    input('press "enter" to exit\n')
    clear_screen()


main()
