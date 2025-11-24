names = ['Квам-Дамн', 'Лук Скамворкер', 'Петард Вейпер', 'Лия Моргала', 'Эдуард Скамворкер']
phones = ['-79899899889', '112', '1', '+09998765432', '0']

book_phones = {
    names[0]: phones[0],
    names[1]: phones[1],
    names[2]: phones[2],
    names[3]: phones[3],
    names[4]: phones[4],
}

user_name = input('Введите имя:  ')
if user_name in book_phones:
    print(f'phones: {book_phones[user_name]}')