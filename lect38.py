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

def enter_dynamic_data():
    lang = input("What language? ")
    version = input("What versiont? ")
    skill = input("What sill level? ")

    c.execute("INSERT INTO example(Language, Version, Skill) VALUES(?, ?, ?)", (lang, version, skill))
    conn.commit()

def read_database():
    what_skill = input("What skill level are we looking for? ")
    what_lang = input("What language?: ")
    sql = "SELECT * FROM example WHERE Skill == ? AND Language = ?"

    for row in c.execute(sql, [(what_skill), (what_lang)]):
        print(row)

def read_database_1():
    sql = "SELECT * FROM example"

    print(20*"*")    
    for row in c.execute(sql):
        print(row)

def update_db():
    print(20*"#")
    sql = "UPDATE example SET Skill = 'Beginner' WHERE Skill = 'beginner'"
    c.execute(sql)
    conn.commit()

def delete_db():
    print(20*"^")
    sql = "DELETE FROM example WHERE Skill = 'Beginner'"
    c.execute(sql)
    conn.commit()
    

#enter_dynamic_data()
#enter_data()
#read_database()
print("Updating Database")
update_db()
read_database_1()
print("Deleting from database")
delete_db()
read_database_1()

conn.close()


