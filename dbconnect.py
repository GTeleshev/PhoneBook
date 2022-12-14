import sqlite3
import os

path = os.getcwd()
print(path)
connstring = f'{path}\phonebook.db'

# импорт просмотр всей базы
def view():
    conn = sqlite3.connect(connstring)
    cursor = conn.cursor()
    data = cursor.execute('''SELECT * FROM PHONEBOOK''')
    tuplePB = []
    for row in data:
        # print(row)
        id = row[0]
        lastname = row[1]
        firstname = row[2]
        phone = row[3]
        description = row[4]
        entry = (id, lastname, firstname, phone, description)
        # entry = row
        tuplePB.append(entry)
    return tuplePB


# вставка записи
def insert(lastname, firstname, phone, description):
    conn = sqlite3.connect(connstring)
    cursor = conn.cursor()
    dbstring = f'''INSERT INTO PHONEBOOK (LASTNAME, FIRSTNAME, PHONE, DESCRIPTION) VALUES 
            ('{lastname}', '{firstname}', '{phone}', '{description}')'''
    cursor.execute(dbstring)
    conn.commit()
    conn.close()


def select_lastname(lastname):
    conn = sqlite3.connect(connstring)
    cursor = conn.cursor()
    dbstring = f'''SELECT * FROM PHONEBOOK WHERE 
            LASTNAME = "{lastname}"'''
    data = cursor.execute(dbstring)
    rows = cursor.fetchall()
    for row in data:
        print(row)
    return rows


def select_full(lastname, firstname, phone, description):
    conn = sqlite3.connect(connstring)
    cursor = conn.cursor()
    dbstring = f'''SELECT * FROM PHONEBOOK WHERE 
            LASTNAME = "{lastname}" AND FIRSTNAME = "{firstname}" AND PHONE = "{phone}" AND DESCRIPTION = "{description}"'''
    data = cursor.execute(dbstring)
    rows = cursor.fetchall()
    for row in data:
        print(row)
    return rows



def delete_by_id(id):
    conn = sqlite3.connect(connstring)
    dbstring = f'DELETE FROM PHONEBOOK WHERE id={id}'
    cursor = conn.cursor()
    cursor.execute(dbstring)
    conn.commit()
