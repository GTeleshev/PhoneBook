import dbconnect
from Notes import Notes

notes = Notes()


def get_notes():
    print(notes.get_all()) #TODO причесать вывод

def add_record():
    data_list = []
    data_list.append(input('Введите фамилию: '))
    data_list.append(input('Введите имя: '))
    data_list.append(input('Введите телефон: '))
    data_list.append(input('Введите описание: '))
    notes.add_note(data_list)
    notes.end()
    main_menu()

def exit_phonebook():
    notes.end()
    exit()

def check_menu(option):
    print('Работает функция №: ', option)


def check_numeric(message, min_, max_):
    out = -100
    check = False
    while not check or out > max_ or out < min_:
        str_out = input(message)
        if not str_out.isdigit():
            check = False
        else:
            out = int(str_out)
            check = True
    return out


def main_menu():
    print("Телефонный справочник x.x")
    options = {1: "Добавление записей",
               2: "Вывод на экран",
               3: "Импорт",
               4: "Экспорт",
               5: "Удаление записей",
               6: "Поиск",
               7: "Завершить работу"}
    functions = {1: add_record,
             2: get_notes,
             3: check_menu,
             4: check_menu,
             5: check_menu,
             6: check_menu,
             7: exit_phonebook}
    for iter in options.keys():
        print(iter, options[iter])
    option = check_numeric("Выберите действие: ", 1, 8)
    print("Выбрано: ", options[option])
    functions[option]() # можно передавать без аргумента "()"
    main_menu()
    return option


main_menu()