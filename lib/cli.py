import sqlite3
from classes.player import Player
from classes.user import User
from classes.World.Room import Room
from helpers import DEBUGGING, VICTORY_LEVEL, WINDOW_WIDTH, debug_print

from prints.print_formats import *
import time


looping = True
high_score = 0


# print methods
def print_cave_outline():
    print()
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


def print_escape_art():
    print()
    print(r"+----------------------------------------------------------------------------+")
    print(r"|  ` : | | | |:  ||  :     `  :  |  |+|: | : : :|   .        `              .|")
    print(r"|         .' ':  ||  |:  |  '       ` || | : | |: : |   .  `           .   :.|")
    print(r"|                `'  ||  |  ' |   *    ` : | | :| |*|  :   :               :||")
    print(r"|        *    *       `  |  : :  |  .      ` ' :| | :| . : :         *   :.|||")
    print(r"|             .`            | |  |  : .:|       ` | || | : |: |          | |||")
    print(r"|      '          .         + `  |  :  .: .         '| | : :| :    .   |:| |||")
    print(r"|         .                 .    ` *|  || :       `    | | :| | :      |:| | |")
    print(r"| .                .          .        || |.: *          | || : :     :|||   |")
    print(r"|        .            .   . *    .   .  ` |||.  +        + '| |||  .  ||`    |")
    print(r"|     .             *              .     +:`|!             . ||||  :.||`     |")
    print(r"| +                      .                ..!|*          . | :`||+ |||`      |")
    print(r"|     .                         +      : |||`        .| :| | | |.| ||`     . |")
    print(r"|       *     +   '               +  :|| |`     :.+. || || | |:`|| `         |")
    print(r"|                            .      .||` .    ..|| | |: '` `| | |`  +        |")
    print(r"|  .       +++                      ||        !|!: `       :| |              |")
    print(r"|              +         .      .    | .      `|||.:      .||    .      .    |")
    print(r"|          '                           `|.   .  `:|||   + ||'     `          |")
    print(r"|  __    +      *                         `'       `'|.    `:                |")
    print(r"|  _  _ __  _  _    ____ ____  ___  __  ____ ____ ____ `.    `.  .    ____,.,|")
    print(r"| ( \/ )  \/ )( \  (  __) ___)/ __)/ _\(  _ (  __|    \    ___,--'--`---'':.:|")
    print(r"|  )  (  O ) \/ (   ) _)\___ ( (__/    \) __/) _) ) D (--'':.:.:.:.::.:.:.:.:|")
    print(r"| (__/ \__/\____/  (____|____/\___)_/\_(__) (____|____/ :.:.:.:.::.:.:.:.::.:|")
    print(r"+----------------------------------------------------------------------------+")
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
        account_info[1],
        account_info[2],
        account_info[3],
        account_info[4],
        account_info[5],
        id=account_info[0],
    )

    # 0 = id, 1 = username, 2 = password, 3 = high score, 4 = times played, 5 = times won
    # print(account_info)

    print_header(login_success_header)
    print(f"\nWelcome back, {account_info[1].upper()}!")

    return current_user


def mainGame(current_user):
    player = Player()
    high_score = current_user.high_score
    highest_level_reached = 0

    game_looping = True
    current_room = Room.create_starting_room()

    while game_looping:
        ##### DEBUGGING
        if DEBUGGING:
            print(" ")
            # debug_print(f"player.health: {player.health}")
            # debug_print(f"player.attack: {player.attack}")
            debug_print(f"current_room: {current_room}")
            debug_print(f"open_paths: {Room.open_paths}")
        #####
        highest_level_reached = max(current_room.level, highest_level_reached)

        if current_room.level != 0 or not current_room.first_time:
            print_line()
            print(
                f"[ Level: {current_room.level} | Health: {player.health} | Attack: {player.attack} ]"
            )

        if current_room.level == VICTORY_LEVEL:
            # print_header(game_won_header)
            print_escape_art()
            new_outcome = "exit"
            current_user.times_won += 1
        else:
            new_outcome = current_room.run_room(
                user=current_user, player=player
            )  # return previous, exit, left, straight, right

        if new_outcome in ["exit", "game over"]:
            if current_room.level != VICTORY_LEVEL:
                # print_header(game_over_header)

                print()
                print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
                print("|" + "{:^{}s}".format("GAME OVER", WINDOW_WIDTH - 2) + "|")
                print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
                print(
                    "| "
                    + "{:<{}s}".format(
                        f"You reached: Level {highest_level_reached}", WINDOW_WIDTH - 3
                    )
                    + "|"
                )
                print("| " + "{:<{}s}".format(f" High Score: {high_score}", WINDOW_WIDTH - 3) + "|")
                print("+" + "-" * (WINDOW_WIDTH - 2) + "+")

                # print(f"\nYou reached: Level {highest_level_reached}!")

            if highest_level_reached > high_score:
                high_score = highest_level_reached

            current_user.update_account_details(
                current_user.username,
                current_user.password,
                high_score,
                current_user.times_played,
                current_user.times_won,
            )

            # print(f"\nHigh Score: {high_score}")
            time.sleep(1)
            game_looping = False

        else:
            current_room = current_room.exit_room(new_outcome)


# logged in, sub menu
def subMenu(current_user):
    current_user = current_user
    menu_looping = True

    while menu_looping:
        choice = print_menu(sub_menu_dict)

        if choice == "1":
            Room.reset_rooms()
            mainGame(current_user)
        elif choice == "2":
            # print_header(account_details_header)

            # print(f"High Score: {current_user.high_score}")
            # print(f"Times Played: {current_user.times_played}")
            # print(f"Times Won: {current_user.times_won}")
            print("                            ")
            print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
            print("|" + "{:^{}s}".format("ACCOUNT DETAILS", WINDOW_WIDTH - 2) + "|")
            print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
            print(
                "| "
                + "{:<{}s}".format(f"High Score: {current_user.high_score}", WINDOW_WIDTH - 3)
                + "|"
            )
            print(
                "| "
                + "{:<{}s}".format(f"Times Played: {current_user.times_played}", WINDOW_WIDTH - 3)
                + "|"
            )
            print(
                "| "
                + "{:<{}s}".format(f"Times Won: {current_user.times_won}", WINDOW_WIDTH - 3)
                + "|"
            )
            print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
            print("")
            input("Press any key to continue: ")
        #             print_header(account_details_header)
        #             current_user.view_account_details(width=WINDOW_WIDTH)
        #  print(f"High Score: {current_user.high_score}")
        # print(f"Times Played: {current_user.times_played}")
        # print(f"Times Won: {current_user.times_won}")
        # input("Press any key to continue: ")
        elif choice == "3":
            current_user.view_enemy_encounters(width=WINDOW_WIDTH)
            # view_enemy_encounters(current_user)
            pass
        elif choice == "x":
            print("\nLogging out...")
            time.sleep(1)
            menu_looping = False
        else:
            print("\nNot a valid input!")


# main menu
while looping:
    print_cave_outline()
    choice = print_menu(main_menu_dict)

    if choice == "1":
        current_user = view_sign_up_menu()
        time.sleep(1)
        if current_user != None:
            subMenu(current_user)
    elif choice == "2":
        current_user = view_log_in_menu()
        time.sleep(1)
        if current_user != None:
            subMenu(current_user)
    elif choice == "x":
        looping = False
        print("Exiting game...")
    else:
        print("Not a valid input!")
