def find_commit_spots(fname):
    commit_every = int()
    with open(fname) as f:
        commit_every = len([commit_every + 1 for _ in f])
        return int(commit_every / int(len(str(commit_every))**2))


import sqlite3

conn = sqlite3.connect(r'TestData/Database/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = r'TestData\mbox-short.txt'
line_counter = 0
commit_every = find_commit_spots(fname)
with open(fname) as f:  
    for line in f:
        if not line.startswith('From: '): continue
        pieces = line.split()
        org = pieces[1].split("@")[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

        line_counter = line_counter + 1
        if line_counter >= commit_every:
            conn.commit()
            line_counter = 0
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
