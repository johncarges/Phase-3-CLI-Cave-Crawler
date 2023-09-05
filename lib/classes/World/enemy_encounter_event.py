from classes.player import Player
from classes.Enemy import Enemy
from classes.user import User
from prints.print_formats import print_basic_menu

user = User.sample_user()
enemy= Enemy.create_from_db(level=10)
player= Player()

