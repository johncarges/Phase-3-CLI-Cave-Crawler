import sqlite3

CONN = sqlite3.connect("./lib/db/cave_crawler.db")
CONN_MAX_AGE = 200
CURSOR = CONN.cursor()


class User:
    def __init__(self, username, password, high_score=0, times_played=0, times_won=0, id=None):
        self.username = username
        self.password = password
        self.high_score = high_score
        self.times_played = times_played
        self.times_won = times_won
        self.id = id

        self.create_user_table()

    @classmethod
    def create_user_table(cls):
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

    def save_account(self):
        sql = "INSERT INTO users ( username, password, high_score, times_played, times_won ) values ( ?, ?, ?, ?, ? )"
        CURSOR.execute(
            sql, (self.username, self.password, self.high_score, self.times_played, self.times_won)
        )
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM users").fetchone()[0]

    # sign up methods
    @classmethod
    def check_new_username(cls, username_input):
        if type(username_input) is str and 2 <= len(username_input) <= 20:
            return username_input
        else:
            print("\nUsername must be a string between 2 and 20 characters.")
            username = input("\nUsername: ")
            return cls.check_new_username(username)

    @classmethod
    def check_new_password(cls, password_input):
        if type(password_input) is str and 2 <= len(password_input) <= 20:
            return password_input
        else:
            print("\nPassword must be a string between 2 and 20 characters.")
            password = input("\nPassword: ")
            return cls.check_new_password(password)

    # log in methods
    @classmethod
    def match_username(cls, username_input):
        sql = f"SELECT * FROM users WHERE username = '{username_input}'"
        count = CURSOR.execute(sql).fetchone()

        if count is None:
            print("\nUsername not found. Please try again.")
            username = input("\nUsername: ")
            return cls.match_username(username)
        else:
            return username_input

    @classmethod
    def match_password(cls, password_input):
        sql = f"SELECT * FROM users WHERE password = '{password_input}'"
        count = CURSOR.execute(sql).fetchone()

        if count is None:
            print("\nPassword not found. Please try again.")
            password = input("\nPassword: ")
            return cls.match_password(password)
        else:
            return password_input

    @classmethod
    def on_successful_login(cls, username, password):
        sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        account_info = CURSOR.execute(sql).fetchone()

        return account_info

    @classmethod
    def update_account_details(cls, username, password, high_score, times_played, times_won):
        sql = f"UPDATE users SET high_score = '{high_score}', times_played = '{times_played + 1}', times_won = '{times_won}' WHERE username = '{username}' AND password = '{password}'"
        CURSOR.execute(sql)
        CONN.commit()

    ### use to reset account details (sqlite3, .open file-path)
    # sql = f"UPDATE users SET high_score = 0, times_played = 0, times_won = 0 WHERE username = 'breelle' AND password = 'isawesome'"

    ## DEBUG METHOD TO USE FIRST USER
    @classmethod
    def sample_user(cls):
        sql = "SELECT * FROM users"
        user_info = CURSOR.execute(sql).fetchone()
        return User(id=user_info[0], username=user_info[1], password=user_info[2])

    def encounter_and_defeated_count(self,enemy_id):
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        sql = f"""
            SELECT COUNT(*) 
            FROM encounters
            WHERE user = {self.id}
            AND enemy = {int(enemy_id)}
        """
        encounter_count = CURSOR.execute(sql).fetchone()[0]
        sql = f"""
            SELECT COUNT(*) 
            FROM encounters
            WHERE user = {self.id}
            AND enemy = {int(enemy_id)}
            AND defeated = TRUE
        """
        defeated_count = CURSOR.execute(sql).fetchone()[0]
        CONN.commit()
        CONN.close()
        return (encounter_count, defeated_count)


    def view_enemy_encounters(self, width):
        CONN = sqlite3.connect("./lib/db/cave_crawler.db")
        CURSOR = CONN.cursor()
        enemies_sql = """
            SELECT name, health, attack, level, description, id 
            FROM enemies
        """
        enemies_list = [list(enemy) for enemy in CURSOR.execute(enemies_sql).fetchall()]
        encountered_sql = f"""
            SELECT DISTINCT enemies.name
            FROM enemies
            INNER JOIN encounters
            ON enemies.id = encounters.enemy
            WHERE encounters.user = {self.id}
        """
        try:
            encountered_enemies = [enemy[0] for enemy in CURSOR.execute(encountered_sql).fetchall()]
        except:
            print("You haven't seen any enemies yet!")
            input("Enter any key to continue: ")
            return
        defeated_sql = f"""
            SELECT DISTINCT enemies.name
            FROM enemies
            INNER JOIN encounters
            ON enemies.id = encounters.enemy
            WHERE encounters.user = {self.id}
            AND encounters.defeated = TRUE 
        """
        defeated_enemies = [enemy[0] for enemy in CURSOR.execute(defeated_sql).fetchall()]
        CONN.close()



        # for index, enemy in enumerate(enemies_list):
        #     if enemy[0] not in encountered_enemies:
        #         enemies_list[index] = ["????", "?", "?", "?", "????", " "]
        #     if enemy[0] in defeated_enemies:
        #         enemy.append("x")
        #     else:
        #         enemy.append(" ")
        
        for index, enemy in enumerate(enemies_list):
            if enemy[0] not in encountered_enemies:
                enemies_list[index] = ["????", "?", "?", "?", "????", " ", " ", " "]
            else:
                enemy.append(self.encounter_and_defeated_count(enemy[5])[0])
                enemy.append(self.encounter_and_defeated_count(enemy[5])[1])
      
            

        print("")
        print(
            "+" + "-" * 21 + "+"+ "-" * 8 + "+" + "-" * 8+ "+" + "-" * 8 + "+" + "-" * 7+ "+"+ "-" * 51+ "+"
        )
        print(
            "| "
            + "{:20}".format("ENEMY")
            + "| "
            + "{:7}".format("SLAIN")
            + "| "
            + "{:7}".format("HEALTH")
            + "| "
            + "{:7}".format("ATTACK")
            + "| "
            + "{:6}".format("LEVEL")
            + "| "
            + "{:{}s}".format("DESCRIPTION", 50)
            + "|"
        )
        print(
            "+"
            + "-" * 21
            + "+"
            + "-" * 8
            + "+"
            + "-" * 8
            + "+"
            + "-" * 8
            + "+"
            + "-" * 7
            + "+"
            + "-" * 51
            + "+"
        )
        for enemy in enemies_list:
            print(
                "| "
                + "{:20}".format(enemy[0])
                + "| "
                + "{:^7}".format(enemy[7])
                + "| "
                + "{:^7}".format(enemy[1])
                + "| "
                + "{:^7}".format(enemy[2])
                + "| "
                + "{:^6}".format(enemy[3])
                + "| "
                + "{:{}s}".format(enemy[4], 50)
                + "|"
            )
            print(
                "+"
                + "-" * 21
                + "+"
                + "-" * 8
                + "+"
                + "-" * 8
                + "+"
                + "-" * 8
                + "+"
                + "-" * 7
                + "+"
                + "-" * 51
                + "+"
            )
        print("")
        input("Press any key to continue: ")

    def view_account_details(self, width):
        print("")
        print("{:>{}s}".format("High Score: ", width // 2) + str(self.high_score))
        print("{:>{}s}".format("Times Played: ", width // 2) + str(self.times_played))
        print("{:>{}s}".format("Times Won: ", width // 2) + str(self.times_won))
        print("")
        input("Press any key to continue: ")
