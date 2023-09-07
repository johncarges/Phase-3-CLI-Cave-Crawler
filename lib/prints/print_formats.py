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
    "options": {"1": "Attack", "2": "Sneak", "3": "Run", "x": "Exit game"},
    "input_header": "Input your choice: ",
}


defeated_enemy_menu_dict = {
    "header": "ENEMY DEFEATED",
    "options": {"1": "Go straight", "2": "Go back", "x": "Exit game"},
    "input_header": "Input your choice: ",
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


starting_room = {
    "options": {"1": "Turn left", "2": "Go straight", "3": "Turn right", "x": "Quit game"},
    "input_header": "Input your choice: ",
}

# enemy_encounter = {
#     "options": {"1": "Attack enemy", "2": "Sneak past", "3": "Run away", "x": "Quit game"},
#     "input_header": "Input your choice: ",
# }

# after_enemy = {
#     "options": {"1": "Attack enemy", "2": "Sneak past", "3": "Run away", "x": "Quit game"},
#     "input_header": "Input your choice: ",
# }

fork_room = {
    "options": {"1": "Turn left", "2": "Turn right", "3": "Go back", "x": "Quit game"},
    "input_header": "Input your choice: ",
}


def print_options(options_dict):
    print()
    if options_dict["options"]:
        for key, value in options_dict["options"].items():
            string = f"{key}. {value}"
            print(string)
    print()
    if options_dict["input_header"]:
        print(options_dict["input_header"], end="")
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


hiking_text = "Your day begins with a peaceful hike through the forest. Surrounded by the serenity of nature, you follow a winding trail deeper into the wilderness. As you venture further, a hidden entrance to a cave catches your eye, its mysteries drawing you in. With only your flashlight to light the way, you enter the cool, dimly lit cavern and begin to explore. But, in a twist of fate, a powerful force strikes the back of your head, plunging you into darkness."
waking_up_text = "When you awake, disoriented and alone, you find yourself deep underground. The feeble glow of your flashlight reveals the harsh reality of your situation. Beside you lays a rusty sword, worn by time. Your journey begins here and your survival depends on the choices you make."
starting_text_first_time = (
    "As your eyes adjust, you see three tunnels ahead of you. Which will you take?"
)
starting_text_after_first = "You find yourself back where you started. Which path will you take?"
# enemy_text = "will change based on enemy..."
fork_text = "You arrive in a dimly lit chamber. Before you, two tunnels beckon."
treasure_text_first_time = "You find a small room. A dead end. However, you spot a treasure chest hidden near the back of the room! Will you open it?"
treasure_text_after_first = "You return to the dead end room with the chest."




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
