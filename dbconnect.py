# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('phonebook.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

data=cursor.execute('''SELECT * FROM PHONEBOOK''')
for row in data:
    print(row)

# Commit your changes in
# the database
conn.commit()

# Closing the connection
conn.close()
