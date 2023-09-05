WINDOW_WIDTH = 40


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

Input your choice: 2         # INPUTS

"""

main_menu_dict = {
    "header": "WELCOME TO CAVE CRAWLER!",
    "options": {
        "1": "Sign Up",
        "2": "Log in",
        "3": "Show enemies",
        "x": "Exit Game"
    },
    "input header": None,
    "inputs": ["Input your choice: "]
}

sign_up_menu_dict = {
    "header": "SIGN UP",
    "options": None,
    "input header": "Enter your account details:",
    "inputs": ["Username:", "Password:"]
}

battle_menu_dict = {
    "header": "What will you do?",
    "options": {
        "1": "Attack",
        "2": "Sneak",
        "3": "Run",
        "x": "Exit Game" 
    },
    "input header": None,
    "inputs": ["Input your choice: "]
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
    "options": {
        "1": "Sign up",
        "2": "Main Menu",
        "3": "Battle",
        "x": "Exit"
    },
    "input header": "Think carefully",
    "inputs": ["Input your choice: "]
}


def print_menu(menu_dict):
    inputs = []
    print("                            ")
    print("+" + "-"*(WINDOW_WIDTH-2) + "+")
    print("|" + "{:^{}s}".format(menu_dict["header"], WINDOW_WIDTH-2) +"|")
    print("+" + "-"*(WINDOW_WIDTH-2) + "+")
    if menu_dict["options"]:
        print("| "+ "{:<{}s}".format("Options:",WINDOW_WIDTH-3) + "|")
        for key, value in menu_dict["options"].items():
            string = f"{key}. {value}"
            print("| " + '{:<{}s}'.format(string, WINDOW_WIDTH-3) + "|")
        print("+" + "-"*(WINDOW_WIDTH-2) + "+")
    print("                            ")
    if menu_dict["input header"]:
        print(" " + '{:25}'.format(menu_dict["input header"]))
        print("                            ")
    
    for input_text in menu_dict["inputs"]:
        new_input = input(input_text+ " ")
        inputs.append(new_input)
    return inputs

if __name__ == "__main__":
    looping=True
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
