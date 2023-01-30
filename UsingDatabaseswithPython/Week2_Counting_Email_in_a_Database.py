import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

#We are going to pretend this is a dictionary
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

#/Users/baeksoyoung/Desktop/mbox.txt
fname = input('Enter file name: ')
if(len(fname) < 1):
    'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # ? -> place holder, this is a way we don't allow SQL injection
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # row -> get information from the database
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    #[0] : email, [1] : count
    print(str(row[0], row[1]))
conn.close()