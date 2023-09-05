from random import randint
from classes.Enemy import Enemy
from classes.encounter import Encounter

class Room:

    ROOM_TYPES = ["start", "fork", "enemy", "dead_end"]

    open_paths = 3

    def __init__(self, level, type=None, previous_room=None):
        self.type = type
        self.level = level
        self.adjacent_rooms = {
            "previous": previous_room, 
            "left": None, 
            "straight": None, 
            "right": None
            }
        # QUESTION - SSOT, should room only save next rooms? Find previous room with lookup?

    def __repr__(self):
        return f"{self.type} room on level {self.level}"

    @classmethod
    def create_new_room(cls, level,previous_room, path):
        """
        for example: In Room room5, when user chooses "left", run Room.new_room(room5, "left", room5.level+1)
        """
        # First, check whether there whether there is more than one open path. If so, don't allow new dead-end
        # TO-DO: add logic to make sure you don't hit three enemies in a row or three forks in a row
        if Room.open_paths > 3: # If too many options, give enemy or treasure
            rand_type = Room.ROOM_TYPES[randint(2,3)]
        elif Room.open_paths > 2: 
            rand_type = Room.ROOM_TYPES[randint(1,3)]
        elif Room.open_paths == 2:
            rand_type = Room.ROOM_TYPES[randint(1,2)]
        else:
            rand_type = "fork" # if only one option left, give a fork

        if rand_type == "fork": 
            Room.open_paths += 1
        elif rand_type == "dead_end": 
            Room.open_paths -= 1
            
        new_room = Room(level, rand_type, previous_room)
        previous_room.adjacent_rooms[path] = new_room # adds this new room to the path dictionary for previous room
        return new_room
        ## Needs functionality to prevent too many dead-ends, 

    @classmethod
    def create_starting_room(cls):
        return Room(level=0, type="start")

    @classmethod
    def starting_room(cls, player, user=None):
        """
            Run upon entering or starting in initial room
        """
        # Eventually, change text if player has already entered room
        print("""
-----------------------------------------------------------------------------
        You find yourself in a large, dark cave. 
        Ahead of you you see three tunnels branching off to the left, straight, and right. 
        """)
        outcome = None
        while not outcome:
            print( """
            Which do you choose? 
            (1) Left
            (2) Straight
            (3) Right
            (x) Exit to main menu
                    """)
            choice = input("Enter your choice: (1, 2, 3, or x): ")
            if choice == "1":
                outcome = "left"
            elif choice == "2":
                outcome = "straight"
            elif choice == "3":
                outcome = "right"
            elif choice == "x":
                outcome = "exit"
            else:
                print("Not a valid input!")
        return outcome

    @classmethod
    def enemy_encounter(cls,player=None, user=None, enemy=None, level=1):
        """
            Run upon entering an enemy-type room
            Player health may change during function run
            Returns outcome: direction
        """
        new_enemy = Enemy.create_from_db(level)
        # new_encounter = Encounter(user=user, enemy=new_enemy)
        # eventually, should loop for battle
        # eventually, should be different text if we return to this room
        print(f"""
-----------------------------------------------------------------------------
        You slay a {new_enemy.name}! 
        Which do you choose? 
        (1) Continue
        (2) Go back
        (x) Exit to main menu
                """)
        
        # new_encounter.update_after_defeat()

        outcome = None
        while not outcome:
            choice = input("Enter your choice: (1, 2,or x): ")
            if choice == "1":
                outcome = "straight"
            elif choice == "2":
                outcome = "previous"
            elif choice == "x":
                outcome = "exit"
            else:
                print("Not a valid response!")
        return outcome

    @classmethod
    def fork_room(cls, player, user=None):
        """
            Run upon entering fork in the road room
        """
        print("""
-----------------------------------------------------------------------------
        You see that the tunnel splits into two up ahead!
        Which do you choose? 
        (1) Go left
        (2) Go right
        (3) Go back
        (x) Exit to main menu
                """)
        outcome = None
        while not outcome:
            choice = input("Enter your choice: (1, 2, 3, or x): ")
            if choice == "1":
                outcome = "left"
            elif choice == "2":
                outcome = "right"
            elif choice == "3":
                outcome = "previous"
            elif choice == "x":
                outcome = "exit"
            else:
                print("Not a valid response!")
        return outcome
    
    @classmethod
    def treasure_room(cls, player, treasure=None,user=None):
        """
            Run upon entering treasure room
        """
        print("""
-----------------------------------------------------------------------------
        You've found a small chamber with a treasure chest!
        You open it and find a better sword!
        It's a dead-end, so you must go back...
            """)
        player.attack += 2
        outcome = None
        while not outcome:
            print("""
                (1) Go back
                (x) Exit game
            """)
            choice = input("Enter your choice: (1 or x): ")
            if choice == "1":
                outcome = "previous"
            elif choice == "x":
                outcome = "exit"
        return outcome

    def enter_room(self, path):
        """(current room, path choice -> room (could be new or already visited) )"""
        if self.adjacent_rooms[path]:
            return self.adjacent_rooms[path] #if room has already been explored, (self.adjacent_rooms[path] not None) return this room
        else:
            new_room =  Room.create_new_room(self.level+1, previous_room=self, path=path)
            return new_room



