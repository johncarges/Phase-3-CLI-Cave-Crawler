from random import randint
from classes.Enemy import Enemy
from classes.encounter import Encounter
from prints.print_formats import *
from prints.print_enemy_art import chest_mist, chest_potion, chest_sword
from classes.World.enemy_encounter_event import enemy_encounter

from helpers import DEBUGGING, debug_print


class Room:
    ROOM_TYPES = ["start", "fork", "enemy", "dead_end"]

    all = []
    start_room = None
    open_paths = 3

    def __init__(self, level, type=None, previous_room=None, enemy=None, treasure=True):
        self.type = type
        self.level = level
        self.enemy = enemy
        self.treasure = treasure
        self.encounter = None
        self.first_time = True
        self.adjacent_rooms = {
            "previous": previous_room,
            "left": None,
            "straight": None,
            "right": None,
        }
        Room.all.append(self)
        # QUESTION - SSOT, should room only save next rooms? Find previous room with lookup?

    def __repr__(self):
        return f"{self.type} room on level {self.level}"

    @classmethod
    def reset_rooms(cls):
        cls.all = []
        cls.open_paths = 3
        cls.start_room = None

    @classmethod
    def create_new_room(cls, level, previous_room, path):
        """
        for example: In Room room5, when user chooses "left", run Room.new_room(room5, "left", room5.level+1)
        """
        # First, check whether there whether there is more than one open path. If so, don't allow new dead-end
        # TO-DO: add logic to make sure you don't hit three enemies in a row or three forks in a row
        if Room.open_paths > 3:  # If too many options, give enemy or treasure
            rand_type = Room.ROOM_TYPES[randint(2, 3)]
        elif Room.open_paths > 2:
            rand_type = Room.ROOM_TYPES[randint(1, 3)]
        elif Room.open_paths == 2:
            rand_type = Room.ROOM_TYPES[randint(1, 2)]
        else:
            rand_type = "fork"  # if only one option left, give a fork

        if rand_type == "fork":
            Room.open_paths += 1
        elif rand_type == "dead_end":
            Room.open_paths -= 1

        new_room = Room(level, rand_type, previous_room)
        previous_room.adjacent_rooms[
            path
        ] = new_room  # adds this new room to the path dictionary for previous room
        return new_room
        ## Needs functionality to prevent too many dead-ends,

    @classmethod
    def create_starting_room(cls):
        cls.start_room = Room(level=0, type="start")
        return cls.start_room

    def starting_room(self, player=None, user=None):
        """
        Run upon entering or starting in initial room
        """
        if self.first_time:
            print_line()
            slow_text("Beginning your adventure...")
            slow_text(
                "\nWould you like to skip the narrative introduction? (Recommended for returning players.)"
            )
            skip = input("\nSkip intro? [y/n]: ")

            if skip == "n":
                slow_text(hiking_text)
                slow_text(waking_up_text)
            elif skip == "y":
                pass
            else:
                print("Not a valid input!")

            slow_text(starting_text_first_time)
            self.first_time = False

        else:
            slow_text(starting_text_after_first)

        outcome = None
        while not outcome:
            choice = print_options(starting_room)

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

    def enemy_room(self, player=None, user=None):
        """
        Run upon entering an enemy-type room.
        Player health may change during function run.
        Returns outcome: direction
        """
        if not self.enemy:
            self.enemy = Enemy.create_from_db(self.level)
            # print(f"New {self.enemy} created!")  # DEBUG
        if self.first_time:
            self.encounter = Encounter(user=user, enemy=self.enemy)
            self.first_time = False

        (outcome, enemy_defeated) = enemy_encounter(user, player, enemy=self.enemy, room=self)

        if enemy_defeated and not self.encounter.defeated:
            # print(f"Adding encounter between {user.username} and {self.enemy.name}")
            self.encounter.update_after_defeat()

        return outcome

    def fork_room(self, player=None, user=None):
        """
        Run upon entering fork in the road room
        """
        slow_text(fork_room_text)
        outcome = None
        while not outcome:
            choice = print_options(fork_room)

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

    def treasure_room(self, player):
        """
        Run upon entering treasure room - called on treasure room instance
        """
        if self.first_time:
            slow_text(treasure_room_first)
            self.first_time = False
        else:
            slow_text(treasure_room_again)
        if self.treasure:
            outcome = None
        else:
            print("There's nothing to see here, so you return to the previous room.")
            input("Press any key to continue: ")
            return "previous"

        while not outcome:
            deciding = True

            while deciding:
                decision = input("\nOpen the chest? [y/n]: ")
                decision.lower()

                if decision == "y":
                    rand_chest = randint(1, 4)

                    if rand_chest == 1:
                        chest_sword()
                        slow_text(
                            "You find a new sword! Your attack is increased by 2. After taking the sword, you return to the previous area."
                        )
                        player.attack += 2

                    elif rand_chest == 2:
                        chest_potion()
                        slow_text(
                            "You find a healing potion! Your health is increased by 1. After taking the potion, you return to the previous area."
                        )
                        player.health += 1
                    elif rand_chest == 3:
                        slow_text("The chest is empty! You sadly return to the previous area.")
                    elif rand_chest == 4:
                        chest_mist()
                        slow_text(
                            "Upon opening the chest, you are engulfed by a sinister mist and cursed with dark magic! Your health is decreased by 2. You stumble back to the previous area."
                        )
                        player.health -= 2
                    self.treasure = False
                    deciding = False
                    outcome = "previous"
                elif decision == "n":
                    slow_text(
                        "You choose to leave the chest untouched and return to the previous area."
                    )
                    deciding = False
                    outcome = "previous"
                else:
                    print("\nNot a valid input!")
        print()
        input("Press any key to continue: ")
        return outcome  # could just be return "previous" ?

    def exit_room(self, path):
        """(current room, path choice -> room (could be new or already visited) )"""
        if self.adjacent_rooms[path]:
            return self.adjacent_rooms[
                path
            ]  # if room has already been explored, (self.adjacent_rooms[path] not None) return this room
        else:
            new_room = Room.create_new_room(self.level + 1, previous_room=self, path=path)
            debug_print(f"New room")
            return new_room

    def run_room(self, user=None, player=None, enemy=None, treasure=None):
        """Runs the relevant loop while user is inside a room"""

        if self.type == "start":
            outcome = self.starting_room()
        elif self.type == "fork":
            outcome = self.fork_room()
        elif self.type == "enemy":
            outcome = self.enemy_room(player, user)
        elif self.type == "dead_end":
            outcome = self.treasure_room(player)
        return outcome
