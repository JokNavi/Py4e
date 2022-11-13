import sqlite3

conn = sqlite3.connect(r'TestData/Database/LongInt.sqlite')
cur = conn.cursor()

try:
    cur.execute('CREATE TABLE Ages ( name VARCHAR(128), age INTEGER)')
except:
    pass
cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Prithivi\', 13);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Marley\', 17);')

cur.execute('INSERT INTO Ages (name, age) VALUES (\'Alisa\', 31);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Johnnie\', 22);')
cur.execute('INSERT INTO Ages (name, age) VALUES (\'Kenadie\', 25);')
conn.commit()
for name in cur:
     print(name)
     
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
print(cur.fetchone())

conn.close()

# Code: http://www.py4e.com/code3/db1.py
