import sqlite3
from classes.user import User
WINDOW_WIDTH = 48


def print_enemy_row(name, health, attack, level, description):
    print("|" + '{:15}'.format(name) 
          + "|" + '{:3}'.format(health)
          + "|" + '{:3}'.format(attack)
          + "|" +'{:3}'.format(level)
          + "|" +'{:{}s}'.format(description, WINDOW_WIDTH-2) + "|")
    print("+" + "-"*(WINDOW_WIDTH-2) +"+")

def view_enemy_encounters(user):
    
    CONN = sqlite3.connect("./lib/db/cave_crawler.db")
    CURSOR = CONN.cursor()
    enemies_sql = """
        SELECT name, health, attack, level, description 
        FROM enemies
    """
    enemies_list = CURSOR.execute(enemies_sql).fetchall()
    encountered_sql = f"""
        SELECT DISTINCT enemies.name
        FROM enemies
        INNER JOIN encounters
        ON enemies.id = encounters.enemy
        WHERE encounters.user = {user.id}
    """
    encountered_enemies = CURSOR.execute(encountered_sql).fetchall()
    defeated_sql = f"""
        SELECT DISTINCT enemies.name
        FROM enemies
        INNER JOIN encounters
        ON enemies.id = encounters.enemy
        WHERE encounters.user = {user.id}
        AND encounters.defeated = TRUE 
    """
    defeated_enemies = CURSOR.execute(defeated_sql).fetchall()
    CONN.close()
    print(enemies_list)
    


    input("Press any key to continue: ")

if __name__ == "__main__":
    CONN = sqlite3.connect("./lib/db/cave_crawler.db")
    CURSOR = CONN.cursor()
    user = User.sample_user()
    view_enemy_encounters(user)
