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
    "dead_end": Room.treasure_room
}

# print methods
def print_login_screen():
    print("                            ")
    print("+--------------------------+")
    print("| WELCOME TO CAVE CRAWLER! |")
    print("+--------------------------+")
    print("| Options:                 |")
    print("| 1. New Game              |")
    print("| 2. Load Game             |")
    print("| x: Exit Game             |")
    print("+--------------------------+")
    print("                            ")


def print_new_game_header():
    print("                            ")
    print("+--------------------------+")
    print("|         NEW GAME         |")
    print("+--------------------------+")
    print("                            ")


def print_load_game_header():
    print("                            ")
    print("+--------------------------+")
    print("|         LOAD GAME        |")
    print("+--------------------------+")
    print("                            ")


# menus
def view_new_game_menu():
    print_new_game_header()
    print("Create an account:")

    # put some checks on these
    username = input("\nUsername: ")
    password = input("Password: ")

    User(username, password)

    deciding = True

    while deciding:
        decision = input("\nCreate account? [y/n]: ")
        decision.lower()

        if decision == "y":
            print(f"\nWelcome, {username.upper()}!")
            print(f"\nHigh Score: 0")
            print("\nBeginning your adventure...")
            mainGame()
            deciding = False
        elif decision == "n":
            print("\nAccount creation canceled.")
            print("Returning to login screen...")
            deciding = False
        else:
            print("\nNot a valid input!")


def view_load_game_menu():
    print_load_game_header()
    print("Enter your account details:")

    # has to match info from database
    username = input("\nUsername: ")
    password = input("Password: ")

    # if it does match
    print(f"\nWelcome back, {username.upper()}!")
    print(f"\nHigh Score: {high_score}")
    print("\nBeginning your adventure...")
    mainGame()



def mainGame():
    game_looping = True
    highest_level_reached = 0
    player = Player()
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
        
        new_outcome = ROOM_FUNCTIONS[current_room.type](player) # return previous, exit, left, straight, right
        print(f"new_outcome: {new_outcome}")
        if new_outcome == "exit":
            return ("Failure", highest_level_reached)
        else:
            current_room = current_room.enter_room(new_outcome)
            

while looping:
    print_login_screen()
    choice = input("Input your choice: ")
    choice = choice.lower()

    if choice == "1":
        view_new_game_menu()
    elif choice == "2":
        view_load_game_menu()
    elif choice == "x":
        looping = False
        print("Exiting game...")
    else:
        print("Not a valid input!")

        
