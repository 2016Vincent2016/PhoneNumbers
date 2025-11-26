names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
phones = ['-79899899889', '112', '1', '+09998765432', '0']

book_phones = {
    names[0]: phones[0],
    names[1]: phones[1],
    names[2]: phones[2],
    names[3]: phones[3],
    names[4]: phones[4],
}

name = input('Введите имя: ')
phone = input('Введите номер телефона (или пусто): ')

if name and phone:
    book_phones[name] = phone

elif name not in book_phones and phone == '':
    print("Нет в телефонной книге")

elif name in book_phones and phone == '':
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')
