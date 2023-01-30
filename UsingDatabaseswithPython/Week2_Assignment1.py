# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":
# Then make sure the table is empty by deleting any rows that you previously inserted, and
# insert these rows and only these rows with the following commands:
# Once the inserts are done, run the following SQL command:
# Find the first row in the resulting record set and enter the long string that looks like
# 53656C696E613333.




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
#[('43656C73693136',), ('4368657272793338',), ('47726569673231',), ('4A656576616E3338',), ('4B7361776572793338',), ('56697267696E69653136',)]


conn.commit()
conn.close()
