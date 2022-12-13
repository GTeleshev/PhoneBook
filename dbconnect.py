import sqlite3
import PhoneClasses


# импорт просмотр всей базы
def view():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    data = cursor.execute('''SELECT * FROM PHONEBOOK''')
    for row in data:
        print(row)
    conn.commit()
    conn.close()
    return data


# вставка записи
def insert(lastname, firstname, phone, description):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    dbstring = f'''INSERT INTO PHONEBOOK (LASTNAME, FIRSTNAME, PHONE, DESCRIPTION) VALUES 
            ('{lastname}', '{firstname}', '{phone}', '{description}')'''
    cursor.execute(dbstring)
    conn.commit()
    conn.close()


def select_lastname(lastname):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    dbstring = f'''SELECT * FROM PHONEBOOK WHERE 
            LASTNAME = "{lastname}"'''
    data = cursor.execute(dbstring)
    rows = cursor.fetchall()
    for row in data:
        print(row)
    return rows


def delete_by_id(id):
    conn = sqlite3.connect('phonebook.db')
    dbstring = f'DELETE FROM PHONEBOOK WHERE id={id}'
    cursor = conn.cursor()
    cursor.execute(dbstring)
    conn.commit()
