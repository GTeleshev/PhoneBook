import dbconnect
import PhoneClasses as PClasses


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
    pass
    functions = {1: check_menu,
             2: check_menu,
             3: check_menu,
             4: check_menu,
             5: check_menu,
             6: check_menu,
             7: check_menu}
    for iter in options.keys():
        print(iter, options[iter])
    option = check_numeric("Выберите действие: ", 1, 8)
    print("Выбрано: ", options[option])
    functions[option](option) # можно передавать без аргумента "()"
    return option


main_menu()