import PhoneClasses
import dbconnect
import PhoneClasses as PhC
data = dbconnect.view()

print(data)
print('---------')
print(data[0])
print('---------')
print(data[1][2])
data1 = dbconnect.select_full('Филатов', 'Сергей', '+79154121444', 'рабочий')
print(data1)

for item in data:
    print(f'id: {item[0]}, {item[1]}, {item[2]}, {item[3]}, {item[4]}')

filatov = PhoneClasses.Entry()
filatov.lastname = 'Филатов'
filatov.firstname = 'Сергей'
filatov.phone = '+79154121444'
filatov.description = 'рабочий'

filatov_id = filatov.get_id()
print('id filatova: ', filatov_id)