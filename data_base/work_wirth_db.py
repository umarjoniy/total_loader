DB_URI = 'postgres://wylwtvjoxbqibu:14daa2435e9d6f550f7d5486151567dcd7981c45d50e747d0718c7667f9bb133@ec2-176-34-105-15.eu-west-1.compute.amazonaws.com:5432/d4j8c2trke9arp'
import psycopg2

base = psycopg2.connect(DB_URI)
cur = base.cursor()


# def sql_start():
#     try:
#         global base, cur
#         base=sq.connect('base_cool.db')
#         cur=base.cursor()
#         if base:
#             print('Data base connected OK!')
#         base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)')
#         base.commit()
#     except sq.Error as e:
#         print(e)

def add_user(id, name):
    try:
        cur.execute('INSERT INTO users(id,username) VALUES (%s,%s)', (id, name))
        base.commit()
    except psycopg2.Error as e:
        print(e)


def check_id(id):
    try:
        cur.execute(f"SELECT id FROM users WHERE id={id}")
        for i in cur:
            return 'Yes'
        return 'No'
    except psycopg2.Error as e:
        print(e)
