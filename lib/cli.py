from classes.player import Player
from classes.user import User
from classes.World.Room import Room

VICTORY_LEVEL = 6

looping = True
high_score = 0

ROOM_FUNCTIONS = {
    "start": Room.starting_room,
    "fork": Room.fork_room,
    "enemy": Room.enemy_encounter,
    "dead_end": Room.treasure_room,
}


# print methods
def print_login_screen():
    print("                            ")
    print("+--------------------------+")
    print("| WELCOME TO CAVE CRAWLER! |")
    print("+--------------------------+")
    print("| Options:                 |")
    print("| 1. Sign Up               |")
    print("| 2. Login In              |")
    print("| x: Exit Game             |")
    print("+--------------------------+")
    print("                            ")


def print_sign_up_header():
    print("                            ")
    print("+--------------------------+")
    print("|         SIGN  UP         |")
    print("+--------------------------+")
    print("                            ")


def print_log_in_header():
    print("                            ")
    print("+--------------------------+")
    print("|          LOG  IN         |")
    print("+--------------------------+")
    print("                            ")


def print_login_success_menu():
    print("                            ")
    print("+--------------------------+")
    print("|     LOGIN SUCCESSFUL     |")
    print("+--------------------------+")
    print("                            ")


def print_game_over_header():
    print("                            ")
    print("+--------------------------+")
    print("|        GAME  OVER        |")
    print("+--------------------------+")
    print("| Options:                 |")
    print("| 1. Play Again            |")
    print("| 2. Account Details       |")
    print("| x: Exit Game             |")
    print("+--------------------------+")
    print("                            ")


def print_account_details_menu():
    print("                            ")
    print("+--------------------------+")
    print("|     ACCOUNT DETAILS      |")
    print("+--------------------------+")
    print("                            ")


def print_sub_menu():
    print("                            ")
    print("+--------------------------+")
    print("|     WILL YOU ESCAPE ?    |")
    print("+--------------------------+")
    print("| Options:                 |")
    print("| 1. Begin Game            |")
    print("| 2. Account Details       |")
    print("| 3. Enemies Encountered   |")
    print("| x: Log Out               |")
    print("+--------------------------+")
    print("                            ")


# menus
def view_sign_up_menu():
    current_user = None

    print_sign_up_header()
    print("Create an account:")
    print("Username and password must be strings between 2 and 20 characters.")

    username_input = input("\nUsername: ")
    username = User.check_new_username(username_input)

    password_input = input("Password: ")
    password = User.check_new_password(password_input)

    deciding = True

    while deciding:
        print("\nPlease review your account details:")
        print(f"\nUsername: {username}")
        print(f"Password: {password}")
        decision = input("\nCreate account? [y/n]: ")
        decision.lower()

        if decision == "y":
            current_user = User(username, password)
            current_user.save_account()
            print(f"\nWelcome, {username.upper()}!")
            print(f"\nHigh Score: 0")
            deciding = False
        elif decision == "n":
            print("\nAccount creation canceled.")
            print("Returning to login screen...")
            deciding = False
        else:
            print("\nNot a valid input!")

    return current_user


def view_log_in_menu():
    current_user = None

    print_log_in_header()
    print("Enter your account details:")

    username_input = input("\nUsername: ")
    username = User.match_username(username_input)

    password_input = input("Password: ")
    password = User.match_password(password_input)

    account_info = User.on_successful_login(username, password)

    current_user = User(
        account_info[1], account_info[2], account_info[3], account_info[4], account_info[5]
    )

    # 0 = id, 1 = username, 2 = password, 3 = high score, 4 = times played, 5 = times won
    # print(account_info)

    print_login_success_menu()
    print(f"\nWelcome back, {account_info[1].upper()}!")
    print(f"\nHigh Score: {account_info[3]}")
    print(f"Times Played: {account_info[4]}")
    print(f"Times Won: {account_info[5]}")

    return current_user


# display once player reaches victory/defeat
def view_game_over_menu():
    print_game_over_header()
    deciding = True

    while deciding:
        choice = input("Input your choice: ")
        choice = choice.lower()

        if choice == "1":
            print("\nBeginning your adventure...")
            # send back to main game with newest high score
            deciding = False
        elif choice == "2":
            print("\nLoading account details...")
            # update account info BEFORE getting to account details menu
            deciding = False
        elif choice == "x":
            print("Exiting game...")
            # quit the game completely
            deciding = False
        else:
            print("Not a valid input!")


# do we actually need this??
def view_account_details_menu(current_user):
    print_account_details_menu()

    print(f"High Score: {current_user.high_score}")
    print(f"Times Played: {current_user.times_played}")
    print(f"Times Won: {current_user.times_won}")

    deciding = True

    while deciding:
        print("\nInput 'begin' to start your adventure.")
        # print("Input 'enemies' to see your enemy encounters.")
        print("Input 'exit' to log out.")

        ready = input("\nInput your choice: ")
        ready.lower()

        if ready == "begin":
            print("\nBeginning your adventure...")
            mainGame(account_info[3])
            deciding = False
        elif ready == "exit":
            print("\nReturning to login screen...")
            deciding = False
        else:
            print("\nNot a valid input!")


def mainGame(current_user):
    player = Player()
    high_score = current_user.high_score
    highest_level_reached = 0

    game_looping = True
    current_room = Room.create_starting_room()

    while game_looping:
        ##### DEBUGGING
        if True:
            print(f"player.health: {player.health}")
            print(f"player.attack: {player.attack}")
            print(f"current_room: {current_room}")
            print(f"current_level: {current_room.level}")
            print(f"open_paths: {Room.open_paths}")
        #####

        if current_room.level == VICTORY_LEVEL:
            return ("victory", VICTORY_LEVEL)

        new_outcome = ROOM_FUNCTIONS[current_room.type](
            player
        )  # return previous, exit, left, straight, right
        print(f"new_outcome: {new_outcome}")
        if new_outcome == "exit":
            return ("Failure", highest_level_reached)
        else:
            current_room = current_room.enter_room(new_outcome)


# logged in, sub menu
def subMenu(current_user):
    current_user = current_user
    menu_looping = True

    while menu_looping:
        print_sub_menu()
        choice = input("Input your choice: ")
        choice = choice.lower()

        if choice == "1":
            mainGame(current_user)
        elif choice == "2":
            print_account_details_menu()
            print(f"High Score: {current_user.high_score}")
            print(f"Times Played: {current_user.times_played}")
            print(f"Times Won: {current_user.times_won}")
        elif choice == "3":
            # view_enemy_encounters(current_user)
            pass
        elif choice == "x":
            print("\nLogging out...")
            menu_looping = False
        else:
            print("\nNot a valid input!")


# main menu
while looping:
    print_login_screen()
    choice = input("Input your choice: ")
    choice = choice.lower()

    if choice == "1":
        current_user = view_sign_up_menu()
        if current_user == None:
            looping = False
        else:
            subMenu(current_user)
    elif choice == "2":
        current_user = view_log_in_menu()
        if current_user == None:
            looping = False
        else:
            subMenu(current_user)
    elif choice == "x":
        looping = False
        print("Exiting game...")
    else:
        print("Not a valid input!")
