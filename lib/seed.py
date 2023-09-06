from prints.print_formats import print_menu
import sqlite3


CONN = sqlite3.connect("./lib/db/cave_crawler.db")
CURSOR = CONN.cursor()


"""
INSTRUCTIONS:

run python lib/db/seed.py to populate enemy list

"""


def create_user_table():
    sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        high_score INTEGER,
        times_played INTEGER, 
        times_won INTEGER
        )
    """
    CURSOR.execute(sql)


user_list = [
    {
        "username": "breelle",
        "password": "isawesome",
        "high_score": 0,
        "times_played": 0,
        "times_won": 0,
    },
    {"username": "john", "password": "iscool", "high_score": 0, "times_played": 0, "times_won": 0},
]


def add_user_to_db(user_list):
    sql = "INSERT INTO users ( username, password, high_score, times_played, times_won ) values (? , ?, ?, ?, ?)"
    for user in user_list:
        CURSOR.execute(
            sql,
            (
                user["username"],
                user["password"],
                user["high_score"],
                user["times_played"],
                user["times_won"],
            ),
        )
        CONN.commit()


def create_enemy_table():
    sql = """
        CREATE TABLE IF NOT EXISTS enemies (
        id INTEGER PRIMARY KEY,
        name TEXT,
        health INTEGER,
        attack INTEGER,
        level INTEGER, 
        description TEXT
        )
    """
    CURSOR.execute(sql)


enemy_list = [
    {
        "name": "Bat",
        "health": 5,
        "attack": 2,
        "level": 1,
        "description": "Creepy flying guy that goes down easy!",
    },
    {"name": "Slime", "health": 3, "attack": 1, "level": 1, "description": "Ew!"},
    {
        "name": "Ghoul",
        "health": 10,
        "attack": 1,
        "level": 2,
        "description": "A slow spooky guy who can barely attack!",
    },
    {
        "name": "Cave Troll",
        "health": 15,
        "attack": 3,
        "level": 5,
        "description": "Run from this guy unless you're feelin' powerful.",
    },
    {
        "name": "Walking Mushroom",
        "health": 2,
        "attack": 0,
        "level": 0,
        "description": "What the heck!",
    },
]


def add_enemy_to_db(enemy_list):
    sql = "INSERT INTO enemies ( name, health, attack, level, description ) values (? , ?, ?, ?, ?)"
    for enemy in enemy_list:
        CURSOR.execute(
            sql,
            (enemy["name"], enemy["health"], enemy["attack"], enemy["level"], enemy["description"]),
        )
        CONN.commit()


def create_encounter_table():
    sql = """
        CREATE TABLE IF NOT EXISTS encounters (
        id INTEGER PRIMARY KEY,
        enemy INTEGER,
        user INTEGER,
        defeated BOOLEAN
        )    
    """

    CURSOR.execute(sql)


debug_menu_dict = {
    "header": "What do you wish to do?",
    "options": {
        "1": "Add enemy",
        "x": "Quit",
    },
    "input_header": "Input your choice: ",
}


if __name__ == "__main__":
    # UNCOMMENT ALL THREE IF YOU DON"T HAVE ENEMY OR ENCOUNTERS TABLE
    looping = True
    while looping:
        choice = print_menu(debug_menu_dict)

        if choice == "1":
            enemy = input("enemy name: ")
            health = input("enemy health: ")
            attack = input("enemy attack: ")
            level = input("enemy level: ")
            description = input("enemy description: ")
            print(f"Name: {enemy}   Health: {health}   Attack: {attack}   Level: {level}")
            print(f"{description}")
            choice = input("Save? [y/n]")
            if choice == "y":
                sql = "INSERT INTO enemies ( name, health, attack, level, description ) values (? , ?, ?, ?, ?)"
                CURSOR.execute(sql, (enemy, health, attack, level, description))
                CONN.commit()
        elif choice == "x":
            break
        else:
            print("not a valid input")

    # create_user_table()
    # add_user_to_db(user_list)
    # create_enemy_table()
    # add_enemy_to_db(enemy_list)
    # create_encounter_table()
    pass
