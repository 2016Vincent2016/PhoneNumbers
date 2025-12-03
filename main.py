# names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
# phones = ['-79899899889', '112', '1', '+09998765432', '0']
#
# book_phones = {
#     names[0]: phones[0],
#     names[1]: phones[1],
#     names[2]: phones[2],
#     names[3]: phones[3],
#     names[4]: phones[4],
# }
#
# name = input('Введите имя: ')
# phone = input('Введите номер телефона (или пусто): ')
#
# if name and phone:
#     book_phones[name] = phone
#
# elif name not in book_phones and phone == '':
#     print("Нет в телефонной книге")
#
# elif name in book_phones and phone == '':
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
#

names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
phones = ['-79899899889', '112', '1', '+09998765432', '0']

book_phones = {
    names[0]: phones[0],
    names[1]: phones[1],
    names[2]: phones[2],
    names[3]: phones[3],
    names[4]: phones[4],
}

while True:
    print("Выберите действие:")
    print("1 — Показать контакт")
    print("2 — Добавить контакт")
    print("3 — Изменить контакт")
    print("4 — Удалить контакт")
    print("0 — Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Пока!")
        break

    elif choice == "1":
        name = input("Введите имя: ")
        if name in book_phones:
            print(f"{name}: {book_phones[name]}")
        else:
            print("Нет в телефонной книге")

    elif choice == "2":
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")
        book_phones[name] = phone
        print("Контакт добавлен.")
        print(book_phones)

    elif choice == "3":
        name = input("Введите имя: ")
        if name in book_phones:
            phone = input("Введите новый номер телефона: ")
            book_phones[name] = phone
            print("Контакт изменён.")
        else:
            print("Нет в телефонной книге")
        print(book_phones)

    elif choice == "4":
        name = input("Введите имя: ")
        if name in book_phones:
            del book_phones[name]
            print("Контакт удалён.")
        else:
            print("Нет в телефонной книге")
        print(book_phones)

    else:
        print("Некорректный выбор. Попробуйте снова.")


