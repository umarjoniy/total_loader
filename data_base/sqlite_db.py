import sqlite3 as sq

def sql_start():
    try:
        global base, cur
        base=sq.connect('base_cool.db')
        cur=base.cursor()
        if base:
            print('Data base connected OK!')
        base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)')
        base.commit()
    except sq.Error as e:
        print(e)

def sql_add_command(id,name):
    try:
        cur.execute('INSERT INTO users VALUES (?,?)',(id,name))
        base.commit()
    except sq.Error as e:
        print(e+1)
def check_id(id):
    try:
        cur.execute(r"SELECT id FROM users WHERE id=?",[id])
        for i in cur:
            return 'Yes'
        return 'No'
    except sq.Error as e:
        print(e+2)