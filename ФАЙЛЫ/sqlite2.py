from sqlite3 import *

con = connect('school.sqlite')
cur = con.cursor()

que_insert = '''
INSERT INTO class (name, surname, mark) VALUES
    ('Василий','Пупкин',3),
    ('Денис','Синицын',4),
    ('Ангелина','Соколова',5),
    ('Саша','Петров',2)
'''

cur.execute(que_insert)
con.commit()


con.close()
