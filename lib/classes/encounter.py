import sqlite3


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
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        CURSOR.execute(sql)
        CONN.commit()
        CONN.close()

    def save_encounter(self):
        sql = "INSERT INTO encounters (enemy, user, defeated) values (?, ?, ?)"
        # print(self.enemy)
        # print(f"self.enemy.id: {self.enemy.id}")
        # print(f"self.user.id: {self.user.id}")
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        CURSOR.execute(sql, (self.enemy.id, self.user.id, self.defeated))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM encounters").fetchone()[0]
        CONN.close()

    def update_after_defeat(self):
        """Run after enemy is defeated. Updates defeated to TRUE"""
        sql = f"""UPDATE encounters 
                SET defeated = TRUE 
                WHERE id = {self.id}"""
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        CURSOR.execute(sql)
        CONN.commit()
        CONN.close()
        self.defeated = True
