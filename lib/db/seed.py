import sqlite3

# EMPTY TABLE FOR GIT PURPOSES

CONN = sqlite3.connect("./cave_crawler.db")
CURSOR = CONN.cursor()

if __name__ == "__main__":
    sql = """DELETE FROM users"""
    CURSOR.execute(sql)
    CONN.commit()
    print("done")