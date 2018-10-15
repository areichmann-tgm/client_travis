import sqlite3

try:

    conn = sqlite3.connect('SQLite-Database.db')
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure sany changes have been committed or they will be lost.
    conn.close()
finally:

    if c:
        c.close()