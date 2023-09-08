import sqlite3
from random import randint


class Enemy:

    

    def __init__(self, name, health, attack, description, id=None):
        self.id = id
        self.name = name
        self.health = health
        self.attack = attack
        self.description = description

    def __repr__(self):
        return f"Enemy {self.name}"

    @classmethod
    def create_from_db(cls, level):
        """Creates new enemy instance from enemy database, 
        based on current level"""
        sql = f"""
            SELECT * FROM enemies
            WHERE level <= {level}
            AND level >= {level-1}
        """
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        possible_enemies = CURSOR.execute(sql).fetchall()
        CONN.close()
        index = randint(0, len(possible_enemies)-1)
        new_enemy = possible_enemies[index]
        return Enemy(
            id=new_enemy[0], 
            name=new_enemy[1],
            health=new_enemy[2],
            attack=new_enemy[3],
            description=new_enemy[5]
            )

    def is_dead(self):
        return self.health <= 0
    
