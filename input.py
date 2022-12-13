import PhoneClasses


def user_input():
    person = PhoneClasses.Entry()
    ln = input('Введите фамилию: ')
    fn = input('Введите имя: ')
    ph = input('Введите телефон: ')
    ds = input('Введите описание: ')
    person.lastname = ln
    person.phone = ph
    person.firstname = fn
    person.description = ds
    person.printentry()
    check = input('Все верно? (д/н): ')
    check = check.lower()
    if check == 'д':
        person.add_db()
    else:
        user_input()

user_input()