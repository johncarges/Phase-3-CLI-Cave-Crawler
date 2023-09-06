from classes.player import Player
from classes.Enemy import Enemy
from classes.user import User
from classes.World.enemy_encounter_event import enemy_encounter
from prints.print_formats import print_menu, battle_menu_dict, defeated_enemy_menu_dict
from random import randint

user = User.sample_user()
enemy= Enemy.create_from_db(level=10)
player= Player()

enemy_encounter(user,player,enemy)