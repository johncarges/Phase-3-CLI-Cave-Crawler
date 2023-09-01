import sqlite3

CONN = sqlite3.connect("./lib/db/cave_crawler.db")
CURSOR = CONN.cursor()


class User:
    def __init__(self, username, password, id=None):
        self.username = username
        self.password = password
        self.id = id
        self.high_score = 0
        self.times_played = 0
        self.times_won = 0

        self.create_user_table()
        self.save_account()

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

    @classmethod
    def match_username(cls, username_input):
        sql = f"SELECT * FROM users WHERE username = '{username_input}'"
        count = CURSOR.execute(sql).fetchone()

        if count is None:
            print("Username not found. Please try again.")

    @classmethod
    def match_password(cls, password_input):
        pass

    @classmethod
    def on_successful_login(cls, username_input, password_input):
        pass
