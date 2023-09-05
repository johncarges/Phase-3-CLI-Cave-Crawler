import sqlite3

CONN = sqlite3.connect("./lib/db/cave_crawler.db")
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

    # @classmethod
    # def on_successful_login(cls, username):
    #     sql = f"SELECT * FROM users WHERE username = '{username}'"
    #     account_info = CURSOR.execute(sql).fetchone()

    #     return account_info

    @classmethod
    def on_successful_login(cls, username, password):
        sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        account_info = CURSOR.execute(sql).fetchone()

        return account_info
