from classes.player import Player
from classes.Enemy import Enemy
from classes.user import User
from prints.print_formats import print_menu, battle_menu_dict, defeated_enemy_menu_dict, slow_text
from prints.print_enemy_art import enemy_print
from helpers import WINDOW_WIDTH
from random import randint
import time


def killed_by_enemy(enemy):
    print(f"\nYou have been slain by the {enemy.name}!\n")
    enemy_print[enemy.name]()
    time.sleep(2)
    return "game over"

def enemy_encounter(user, player, enemy, room=None, enemy_defeated=False):
    """
    Runs enemy encounter - updates player and enemy health.
    Returns direction: back, forward, game over, or quit.
    Also returns encounter outcome: victory, encounter, already encountered
    """

    looping = True
    if enemy.is_dead():
        slow_text(f"You stand over the lifeless body of the {enemy.name}.")
        # time.sleep(1)
        while looping:
            choice = print_menu(defeated_enemy_menu_dict)

            if choice == "1":
                outcome = "straight"
                break
            elif choice == "2":
                outcome = "previous"
                break
            elif choice == "x":
                outcome = "exit"
                break
            else:
                print("Not a valid input!")
                continue
    else:
        slow_text(f"You come across an enemy {enemy.name}!")
        enemy_print[enemy.name]()
        enemy_defeated = False
        while looping:
            print(f"\n{'{:>11}'.format(user.username)}: {'[♥]'*player.health}")
            print(f"{'{:>11}'.format(enemy.name)}: {'[♥]'*enemy.health}")

            choice = print_menu(battle_menu_dict)
            print("\n")
            print_out = []
            if choice == "1":
                print_out.append(f"You attack the {enemy.name}! You deal {player.attack} damage.")
                enemy.health -= player.attack
                if enemy.is_dead():
                    print_out.append(f"\nThe {enemy.name} is no more!")
                    enemy_defeated = True
                    
                    for item in print_out:
                        print(item)
                    return enemy_encounter(
                        user, player, enemy, enemy_defeated=enemy_defeated
                    )  # tricky little recursion :|
                else:
                    print_out.append(
                        f"\nThe {enemy.name} attacks you back for {enemy.attack} hearts!"
                    )
                    player.health -= enemy.attack
                    
                    if player.health <= 0:
                        outcome = killed_by_enemy(enemy)
                        break
            elif choice == "2":
                coin = randint(0, 1)
                if coin == 0:
                    print(f"You successfully snuck by the {enemy.name}!\n")
                    input("Press any key to continue: ")
                    outcome = "straight"
                    break
                else:
                    print(f"The {enemy.name} sees you and attacks!")
                    player.health -= enemy.attack
                    if player.health <= 0:
                        outcome = killed_by_enemy(enemy)
                        break
            elif choice == "3":
                print("You decide to return to safety!\n")

                outcome = "previous"
                break
            elif choice == "x":
                outcome = "exit"
                break
            else:
                print("Not a valid input!")
            for item in print_out:
                print(item)

    return (outcome, enemy_defeated)
