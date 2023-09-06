import sqlite3

CONN = sqlite3.connect("./lib/db/cave_crawler.db")
CURSOR = CONN.cursor()


class Encounter:

    def __init__(self, user, enemy, id=None):
        self.id = id
        self.user = user
        self.enemy = enemy
        self.defeated = False
        
        self.create_encounter_table()
        self.save_encounter()

    @classmethod
    def create_encounter_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS encounters (
            id INTEGER PRIMARY KEY,
            enemy INTEGER,
            user INTEGER,
            defeated BOOLEAN
            )    
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save_encounter(self):
        sql = "INSERT INTO encounters (enemy, user, defeated) values (?, ?, ?)"
        print(self.enemy)
        print(f"self.enemy.id: {self.enemy.id}")
        print(f"self.user.id: {self.user.id}")
        CURSOR.execute(sql, (self.enemy.id, self.user.id, self.defeated))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM encounters").fetchone()[0]

    def update_after_defeat(self):
        """Run after enemy is defeated. Updates defeated to TRUE"""
        sql = f"""UPDATE encounters 
                SET defeated = TRUE 
                WHERE id = {self.id}"""
        CURSOR.execute(sql)
        CONN.commit()





