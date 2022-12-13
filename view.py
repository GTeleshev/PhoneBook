import dbconnect

data = dbconnect.view()

print(data)
print('---------')
print(data[0])
print('---------')
print(data[1][2])
data1 = dbconnect.select_full('Филатов', 'Сергей', '+79154121444', 'рабочий')
print(data1)