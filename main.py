import dbconnect
import PhoneClasses as PClasses

dbconnect.view()

petrov = PClasses.Entry(lastname='Петров', firstname='Александр', phone='+7954318795',description='рабочий')

print(petrov.lastname)
print(petrov.firstname)
print(petrov.phone)
print(petrov.description)

sidorov = PClasses.Entry()
sidorov.firstname = 'Алексей'
sidorov.lastname = 'Сидоров'
sidorov.phone = '123'
sidorov.description = 'домашний'

# print(sidorov.lastname)
# print(sidorov.firstname)
# print(sidorov.phone)
# print(sidorov.description)

# sidorov.add_db()

dbconnect.select_lastname(petrov.lastname)
dbconnect.select_lastname('Филатов')
rows = dbconnect.select_lastname('Филатов')
# print(rows)
# print(type(rows))

# PClasses.Entry.printentry(petrov)

# dbconnect.insert(petrov.lastname, petrov.firstname, petrov.phone, petrov.description)
# PClasses.Entry.add_db(petrov)
# dbconnect.delete_by_id(10)
dbconnect.view()