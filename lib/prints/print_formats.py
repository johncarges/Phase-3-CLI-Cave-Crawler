import time
import re
from helpers import DEBUGGING, WINDOW_WIDTH


"""
+--------------------------+
| WELCOME TO CAVE CRAWLER! | #HEADER
+--------------------------+
| Options:                 |
| 1. Sign Up               | # OPTIONS
| 2. Login In              |
| x: Exit Game             |
+--------------------------+

Input your choice below      # INPUT HEADER

"""

main_menu_dict = {
    "header": "WELCOME TO CAVE CRAWLER!",
    "options": {"1": "Sign Up", "2": "Log In", "x": "Exit Game"},
    "input_header": "Input your choice: ",
}

sub_menu_dict = {
    "header": "CAVE CRAWLER",
    "options": {
        "1": "Begin Game",
        "2": "Account Details",
        "3": "Enemies Encountered",
        "x": "Log Out",
    },
    "input_header": "Input your choice: ",
}


battle_menu_dict = {
    "header": "BATTLE",
    "options": {"1": "Attack", "2": "Sneak", "3": "Run", "x": "Exit Game"},
    "input_header": "Input your choice: ",
}


defeated_enemy_menu_dict = {
    "header": "What will you do?",
    "options": {
        "1": "Go Forward",
        "2": "Go Back",
        "x": "Exit Game" 
    },
    "input_header": None

}

test_menu = {
    "header": "Which menu do you want to see?",
    "options": {"1": "Sign up", "2": "Main Menu", "3": "Battle", "x": "Exit"},
    "input_header": "Input your choice: ",
}


def print_menu(menu_dict):
    print("                            ")
    print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print("|" + "{:^{}s}".format(menu_dict["header"], WINDOW_WIDTH - 2) + "|")
    print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
    if menu_dict["options"]:
        # print("| " + "{:<{}s}".format("Options:", WINDOW_WIDTH - 3) + "|")
        for key, value in menu_dict["options"].items():
            string = f"{key}. {value}"
            print("| " + "{:<{}s}".format(string, WINDOW_WIDTH - 3) + "|")
        print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print("                            ")
    if menu_dict["input_header"]:
        print(menu_dict["input_header"], end="")
        choice = input()
        choice.lower()
        return choice


sign_up_header = "SIGN UP"
log_in_header = "LOG IN"
login_success_header = "LOGIN SUCCESSFUL"
account_details_header = "ACCOUNT DETAILS"
game_over_header = "GAME OVER"
game_won_header = "YOU ESCAPED!!!"


def print_header(header):
    print("                            ")
    print("+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print("|" + "{:^{}s}".format(header, WINDOW_WIDTH - 2) + "|")
    print("+" + "-" * (WINDOW_WIDTH - 2) + "+")

# prints an empty line, "types" out the text, prints another empty line
# TALK ABOUT WHERE TO PUT THIS/IF WE EVEN WANT IT.
def slow_text(text, delay=0.03):
    if DEBUGGING:
        print(text)
    else:
        print()
        sentences = re.split(r"(?<=[.!?])\s+", text)

        for sentence in sentences:
            for char in sentence:
                print(char, end="", flush=True)
                time.sleep(delay)
            print()
            time.sleep(0.5)


if __name__ == "__main__":
    looping = True
    while looping:
        choice = print_menu(test_menu)[0]
        if choice == "1":
            pass
        elif choice == "2":
            menu = main_menu_dict
        elif choice == "3":
            menu = battle_menu_dict
        elif choice == "x":
            looping = False
            break
        else:
            print("Not a valid input!")
            continue

        return_value = print_menu(menu)
        print(f"Input received: {return_value}")
