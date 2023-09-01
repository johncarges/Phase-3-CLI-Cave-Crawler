from classes.player import Player
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


def mainGame():
    game_looping = True
    highest_level_reached = 0
    player = Player()
    current_room = Room.create_starting_room()
    while game_looping:
    
        ##### DEBUGGING
        print(f"player.health: {player.health}")
        print(f"player.attack: {player.attack}")
        print(f"current_room: {current_room}")
        print(f"current_level: {current_room.level}")
        #####
        
        if current_room.level == VICTORY_LEVEL:
            return ("victory", VICTORY_LEVEL)
        
        new_outcome = ROOM_FUNCTIONS[current_room.type](player) # return previous, exit, left, straight, right
        print(f"new_outcome: {new_outcome}")
        if new_outcome == "exit":
            return ("Failure", highest_level_reached)
        else:
            current_room = current_room.enter_room(new_outcome)
            
# MAIN MENU
print(f"""
        WELCOME TO CAVE CRAWLER!
        High Score: {high_score}
        To begin, press 'x'
        To exit, enter 'quit'
          """)
while looping:
    choice = input("Begin your adventure? ")
    if choice == "x":
        (final_outcome, highest_level_reached) = mainGame()
        print("""
------------------------------------------------------------
              """)
        if final_outcome == "victory":
            print("Congratulations! You Did it!")
        elif final_outcome == "defeat":
            print("Thank you for playing!")
            print(f"You made it to level {highest_level_reached}")
        high_score = max(highest_level_reached, high_score)

        print(f"""
        High Score: {high_score}
        To begin again, press 'x'
        To exit, enter 'quit'     
              """)

    elif choice == "quit":
        looping = False
    else:
        print("Not a valid input!")
    
