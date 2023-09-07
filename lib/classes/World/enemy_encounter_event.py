from classes.player import Player
from classes.Enemy import Enemy
from classes.user import User
from prints.print_formats import print_menu, battle_menu_dict, defeated_enemy_menu_dict, slow_text
from random import randint

user = User.sample_user()
enemy = Enemy.create_from_db(level=10)
player = Player()


def enemy_encounter(user, player, enemy, room=None, enemy_defeated=False):
    """
    Runs enemy encounter - updates player and enemy health.
    Returns direction: back, forward, game over, or quit.
    Also returns encounter outcome: victory, encounter, already encountered
    """

    looping = True
    if enemy.is_dead():
        slow_text(f"You stand over the dead {enemy.name}.")
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
        enemy_defeated = False
        while looping:
            print(f"\n{'{:>15}'.format(user.username)}: {'[♥]'*player.health}")
            print(f"{'{:>15}'.format(enemy.name)}: {'[♥]'*enemy.health}")

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
                    print_out.append(f"\nThe {enemy.name} attacks you back for {enemy.attack} hearts!")
                    player.health -= enemy.attack
                    if player.health <= 0:
                        outcome = "game over"
                        break
            elif choice == "2":
                coin = randint(0, 1)
                if coin == 0:
                    print_out.append(f"\nYou successfully snuck by the {enemy.name}!")
                    input("Press any key to continue: ")
                    outcome = "straight"
                    break
                else:
                    print_out.append(f"\nThe {enemy.name} sees you and attacks!")
                    player.health -= enemy.attack
                    if player.health <= 0:
                        outcome = "game over"
                        break
            elif choice == "3":
                print("\nYou decide to return to safety!")
                outcome = "previous"
                break
            elif choice == "x":
                outcome = "exit"
                break
            else:
                print("Not a valid input!")
            for item in print_out:
                print(item)

    print(f"outcome: {outcome}")
    return (outcome, enemy_defeated)
