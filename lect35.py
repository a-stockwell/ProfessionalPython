import sqlite3

conn = sqlite3.connect('tutorial.db')

c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Novice')")
    c.execute("INSERT INTO example VALUES('Python', 3.5, 'Expert')")
    conn.commit()


conn.close()
