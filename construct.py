from model import Phonebook
import datetime as dt

action = int(input('Введите 1, для добавления контакта\n'
                   'Введите 2, для просмотра контактов \n'))
id = dt.datetime.now()
if action == 1:

    while True:
        name = input('Введите имя: \n- ')
        if name.lower() == 'stop':
            break
        number = input('Введите номер: \n- ')
        if number == str:
            print('Введите числовое значение')
        else:
            id = Phonebook()
            id.add_contact(name, number)
            with open('phonebook.txt', 'a') as f:
                f.write(f'{id.get_contact()}')
                f.write("\n")
dict_data = []


if action == 2:

    with open('phonebook.txt', 'r') as f:
        for key in f:
            dict_data.append(key)

    print(*dict_data)





