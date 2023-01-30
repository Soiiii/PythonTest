import sqlite3

conn = sqlite3.connect('Ages.sqlite')
cur = conn.cursor()
row = []
cur.execute('CREATE TABLE Ages (name VARCHAR(128),age INTEGER)')
cur.execute('DELETE FROM Ages')
records = [('Ksawery', 38), ('Celsi', 16), ('Jeevan', 38), ('Greig', 21), ('Virginie', 16), ('Cherry', 38)]

cur.executemany('INSERT INTO Ages VALUES(?,?);', records)


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
print(cur.fetchall())
conn.commit()
conn.close()