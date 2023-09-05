import sqlite3


CONN = sqlite3.connect("./lib/db/cave_crawler.db")
CURSOR = CONN.cursor()


"""
INSTRUCTIONS:

run python lib/db/seed.py to populate enemy list

"""


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
    {"name": "Bat", "health": 5, "attack": 2, "level": 1, "description": "Creepy flying guy that goes down easy!"},
    {"name": "Slime", "health": 3, "attack": 1, "level": 1, "description":"Ew!" },
    {"name": "Ghoul", "health": 10, "attack": 1, "level": 2, "description":"A slow spooky guy who can barely attack!" },
    {"name": "Cave Troll", "health": 15, "attack": 3, "level": 5, "description":"Run from this guy unless you're feelin' powerful." },
    {"name": "Walking Mushroom", "health": 2, "attack": 0, "level": 0, "description":"What the heck!" }
    
]
def add_enemy_to_db(enemy_list):
    sql = "INSERT INTO enemies ( name, health, attack, level, description ) values (? , ?, ?, ?, ?)"
    for enemy in enemy_list:
        CURSOR.execute(sql, (enemy["name"], enemy["health"], enemy["attack"],enemy["level"],enemy["description"]))
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


if __name__ == "__main__":
    # UNCOMMENT ALL THREE IF YOU DON"T HAVE ENEMY OR ENCOUNTERS TABLE

    #create_enemy_table()
    #add_enemy_to_db(enemy_list)
    #create_encounter_table()
    pass