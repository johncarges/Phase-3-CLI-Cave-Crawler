WINDOW_WIDTH = 45
LEFT_MARGIN = " "*4


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

Input your choice: 2         # INPUT

"""

main_menu_dict = {
    "header": "WELCOME TO CAVE CRAWLER!",
    "options": {"1": "Sign Up", "2": "Log In", "x": "Exit Game"},
    "input_header": "Input your choice: ",
}

sub_menu_dict = {
    "header": "WILL YOU ESCAPE?",
    "options": {
        "1": "Begin Game",
        "2": "Account Details",
        "3": "Enemies Encountered",
        "x": "Log Out",
    },
    "input_header": "Input your choice: "
}


battle_menu_dict = {
    "header": "BATTLE",
    "options": {"1": "Attack", "2": "Sneak", "3": "Run", "x": "Exit Game"},
    "input_header": "Input your choice: ",
}

game_over_dict = {
    "header": "GAME OVER",
    "options": {"1": "Play Again", "2": "Main Menu"},
    "input_header": "Input your choice: ",
}

defeated_enemy_menu_dict = {
    "header": "What will you do?",
    "options": {
        "1": "Go Forward",
        "2": "Go Back",
        "x": "Exit Game" 
    },
    "input header": None,
    "inputs": ["Input your choice: "]
}

test_menu = {
    "header": "Which menu do you want to see?",
    "options": {"1": "Sign up", "2": "Main Menu", "3": "Battle", "x": "Exit"},
    "input_header": "Input your choice: ",
}


def print_menu(menu_dict):
    print(LEFT_MARGIN +"                            ")
    print(LEFT_MARGIN +"+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print(LEFT_MARGIN +"|" + "{:^{}s}".format(menu_dict["header"], WINDOW_WIDTH - 2) + "|")
    print(LEFT_MARGIN +"+" + "-" * (WINDOW_WIDTH - 2) + "+")
    if menu_dict["options"]:
        # print(LEFT_MARGIN +"| " + "{:<{}s}".format("Options:", WINDOW_WIDTH - 3) + "|")
        for key, value in menu_dict["options"].items():
            string = f"{key}. {value}"
            print(LEFT_MARGIN +"| " + "{:<{}s}".format(string, WINDOW_WIDTH - 3) + "|")
        print(LEFT_MARGIN +"+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print(LEFT_MARGIN +"                            ")
    if menu_dict["input_header"]:
        print(LEFT_MARGIN +menu_dict["input_header"], end="")
        choice = input()
        choice.lower()

    return choice


sign_up_header = "SIGN UP"
log_in_header = "LOG IN"
login_success_header = "LOGIN SUCCESSFUL"
account_details_header = "ACCOUNT DETAILS"


def print_header(header):
    print(LEFT_MARGIN +"                            ")
    print(LEFT_MARGIN +"+" + "-" * (WINDOW_WIDTH - 2) + "+")
    print(LEFT_MARGIN +"|" + "{:^{}s}".format(header, WINDOW_WIDTH - 2) + "|")
    print(LEFT_MARGIN +"+" + "-" * (WINDOW_WIDTH - 2) + "+")


if __name__ == "__main__":
    looping = True
    while looping:
        choice = print_menu(test_menu)[0]
        if choice == "1":
            menu = sign_up_menu_dict
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
