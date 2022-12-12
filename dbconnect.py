# импорт
import sqlite3

# подключение к базе
conn = sqlite3.connect('phonebook.db')

# SQL-запросы
cursor = conn.cursor()

data=cursor.execute('''SELECT * FROM PHONEBOOK''')
for row in data:
    print(row)

# коммит изменений
conn.commit()

# закрытие соединения
conn.close()
