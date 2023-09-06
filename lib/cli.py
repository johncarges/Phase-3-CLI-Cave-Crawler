from classes.player import Player
from classes.user import User
from classes.World.Room import Room

from prints.print_formats import *
import time

VICTORY_LEVEL = 6
DEBUGGING = False

looping = True
high_score = 0

# print methods
def print_cave_outline():
    print("+--------------------------------------------------------------------------------+")
    print("|                    /   \              /'\       _                              |")
    print("|\_..           /'.,/     \_         .,'   \     / \_                            |")
    print("|    \         /            \      _/       \_  /    \     _                     |")
    print("|     \__,.   /              \    /           \/.,   _|  _/ \                    |")
    print("|          \_/                \  /',.,''\      \_ \_/  \/    \                   |")
    print("|                           _  \/   /    ',../',.\    _/      \                  |")
    print("|             /           _/ \  \  /    |         \  /.,/'\   _\                 |")
    print("|           _/           /    \  \_     |          \/      \_/  \                |")
    print("|          /      \     |      |   \__   \          \_       \   \_              |")
    print("|                  \   /       |      \   \           \       \    \             |")
    print("|                   \  |        \      \___            \_      \_   \            |")
    print("|                    \|          |____.'  /\_            \       \   \_          |")
    print("|                    /'.,___________...,,'   \            \   \        \         |")
    print("|                   /       \          |      \    |__     \   \_       \        |")
    print("|                 _/        |           \      \_     \     \    \       \_      |")
    print("|      ___  __  _  _ ____     ___ ____  __  _  _ __   ____ ____   \         \    |")
    print("|     / __)/ _\/ )( (  __)   / __|  _ \/ _\/ )( (  ) (  __|  _ \   \__       \   |")
    print("|    ( (__/    \ \/ /) _)   ( (__ )   /    \ /\ / (_/\) _) )   /      \       \  |")
    print("|     \___)_/\_/\__/(____)   \___|__\_)_/\_(_/\_)____(____|__\_)               \ |")
    print("+--------------------------------------------------------------------------------+")
    time.sleep(1)


# menus
def view_sign_up_menu():
    current_user = None

    print_header(sign_up_header)
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

    print_header(log_in_header)
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

    print_header(login_success_header)
    print(f"\nWelcome back, {account_info[1].upper()}!")
    print(f"\nHigh Score: {account_info[3]}")
    print(f"Times Played: {account_info[4]}")
    print(f"Times Won: {account_info[5]}")

    return current_user


# display once player reaches victory/defeat
def view_game_over_menu():
    print_menu(game_over_dict)
    deciding = True

    while deciding:
        choice = input("Input your choice: ")
        choice = choice.lower()

        if choice == "1":
            print("\nBeginning your adventure...")
            # send back to main game with newest high score
            deciding = False
        elif choice == "2":
            print("\nReturning to main menu...")
            deciding = False
        else:
            print("Not a valid input!")


def view_account_details_menu(current_user):
    print_header(account_details_header)

    print(f"High Score: {current_user.high_score}")
    print(f"Times Played: {current_user.times_played}")
    print(f"Times Won: {current_user.times_won}")


def mainGame(current_user):
    player = Player()
    high_score = current_user.high_score
    highest_level_reached = 0

    game_looping = True
    current_room = Room.create_starting_room()

    while game_looping:
        ##### DEBUGGING
        if DEBUGGING:
            print(f"player.health: {player.health}")
            print(f"player.attack: {player.attack}")
            print(f"current_room: {current_room}")
            print(f"current_level: {current_room.level}")
            print(f"open_paths: {Room.open_paths}")
        #####

        if current_room.level == VICTORY_LEVEL:
            return ("victory", VICTORY_LEVEL)
         
        # return previous, exit, left, straight, right
        new_outcome = current_room.run_room(player=player, user=current_user)

        if new_outcome == "exit":
            print(Room.all)
            return ("Failure", highest_level_reached)
        else:
            current_room = current_room.enter_room(new_outcome)


# logged in, sub menu
def subMenu(current_user):
    current_user = current_user
    menu_looping = True

    while menu_looping:
        choice = print_menu(sub_menu_dict)

        if choice == "1":
            mainGame(current_user)
        elif choice == "2":
            print_header(account_details_header)
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
    print_cave_outline()
    choice = print_menu(main_menu_dict)

    if choice == "1":
        current_user = view_sign_up_menu()
        if current_user != None:
            subMenu(current_user)
    elif choice == "2":
        current_user = view_log_in_menu()
        if current_user != None:
            subMenu(current_user)
    elif choice == "x":
        looping = False
        print("Exiting game...")
    else:
        print("Not a valid input!")
