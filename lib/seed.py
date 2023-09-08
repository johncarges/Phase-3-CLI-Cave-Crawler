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
        "username": "BreElle",
        "password": "isawesome",
        "high_score": 6,
        "times_played": 9,
        "times_won": 9,
    },
    {
        "username": "John",
        "password": "iscool",
        "high_score": 6,
        "times_played": 10,
        "times_won": 10,
    },
    {
        "username": "Curtis",
        "password": "luvspearls",
        "high_score": 2,
        "times_played": 21,
        "times_won": 0,
    },
    {
        "username": "Teddy",
        "password": "thebear",
        "high_score": 6,
        "times_played": 3,
        "times_won": 2,
    },
    {
        "username": "Hiro",
        "password": "thegenius",
        "high_score": 6,
        "times_played": 4,
        "times_won": 3,
    },
    {
        "username": "Farhan",
        "password": "thebaker",
        "high_score": 6,
        "times_played": 2,
        "times_won": 2,
    },
    {
        "username": "Tess",
        "password": "thegreat",
        "high_score": 6,
        "times_played": 7,
        "times_won": 4,
    },
    {
        "username": "Thomas",
        "password": "thewolf",
        "high_score": 6,
        "times_played": 3,
        "times_won": 2,
    },
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

def delete_user_by_name(name):
    sql = f"""
        DELETE FROM users
        WHERE username = {name}
    """
    CURSOR.execute(sql)



enemy_list = [
    {
        "name": "Bat",
        "health": 5,
        "attack": 2,
        "level": 1,
        "description": "A little guy with glowing eyes amd sharp fangs.",
    },
    {
        "name": "Slime",
        "health": 3,
        "attack": 1,
        "level": 1,
        "description": "Ew!",
    },
    {
        "name": "Centaur",
        "health": 8,
        "attack": 4,
        "level": 4,
        "description": "Half-human, half-horse warrior.",
    },
    {
        "name": "Griffin",
        "health": 15,
        "attack": 4,
        "level": 5,
        "description": "A majestic lion-eagle beast.",
    },
    {
        "name": "Phoenix",
        "health": 7,
        "attack": 3,
        "level": 4,
        "description": "Beware: this bird is not your friend.",
    },
    {
        "name": "Skeleton",
        "health": 5,
        "attack": 2,
        "level": 2,
        "description": "Rattle, rattle.",
    },
    {
        "name": "Unicorn",
        "health": 8,
        "attack": 10,
        "level": 5,
        "description": "It's horn can pierce the sky.",
    },
    {
        "name": "Bear",
        "health": 7,
        "attack": 4,
        "level": 3,
        "description": "A fierce, roaring predator",
    },
    {
        "name": "Big Cat",
        "health": 9,
        "attack": 3,
        "level": 2,
        "description": "The stealthiest of foes.",
    },
    {
        "name": "Giant Ant",
        "health": 6,
        "attack": 4,
        "level": 3,
        "description": "An absolute menace in insect-form.",
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


def delete_enemy_from_db():
    sql = "DELETE FROM enemies"
    CURSOR.execute(sql)
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


def delete_encounters_from_db():
    sql = "DELETE FROM encounters"
    CURSOR.execute(sql)
    CONN.commit()


debug_menu_dict = {
    "header": "What do you wish to do?",
    "options": {
        "1": "Add enemy",
        "x": "Quit",
    },
    "input_header": "Input your choice: ",
}

def add_enemy_by_command_line():
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

if __name__ == "__main__":

   

    # create_user_table()
    # add_user_to_db(user_list)
    # create_enemy_table()
    # delete_enemy_from_db()
    # add_enemy_to_db(enemy_list)
    # create_encounter_table()
    # delete_encounters_from_db()
    #delete_user_by_name("johncarges")
    add_user_to_db(user_list)
    delete_enemy_from_db()
    delete_encounters_from_db()
    add_enemy_to_db(enemy_list)