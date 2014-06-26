import sqlite3 as sqlite

# Create a new in-memory DB and a cursor
#
con = sqlite.connect(':memory:')
cur = con.cursor()

# The table is named 'frames'
# The columns are: a running ID, and a data blob
#
cur.execute('''
    create table frames (
        id integer primary key,
        data blob)''')

# Shove some data into the table. The data stored
# using the sqlite.Binary type, which means a BLOB.
#
cur.execute('''
    insert into frames values (null, ?)''',
    (sqlite.Binary('\0' * 10 + '\x12'),))
cur.execute('''
    insert into frames values (null, ?)''',
    (sqlite.Binary('\x01\x42\x55'),))
code = sqlite.Binary('\x01\x42\x55')
print code
# Now read it back. When BLOBs are read, they're
# converted to Python buffers of type 'buffer'
#
for row in cur.execute("select * from frames"):
    print row[0], str(row[1]).encode('hex')

cur.close()
con.close()