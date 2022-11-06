from sqlite3 import *

con = connect('school.sqlite')
cur = con.cursor()

que_create = '''
CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    mark INTEGER
) 
'''

cur.execute(que_create)
con.commit()


con.close()
