param_insert = ('Имя', 'Фамилия', 'Год Рождения', 'Город проживания', 'Эл почта', 'телефон')
in_parametrs =''
def user_data_get(name='', family='', bird_year='', city='', email='', phone=''):
    if name == '':
        return 'Не введени имя'
    elif family == '':
        return 'Не введена фамилмя'
    elif bird_year == '':
        return 'Не введен год рождения'
    elif city == '':
        return 'Нет введен город проживанмя'
    elif email == '':
        return 'Не введен эл адрес'
    elif phone == '':
        return 'Не введен номер телефона'
    else:
        user_dict = dict(name=name, family=family, bird_year=bird_year, city = city, email = email, phone = phone)
        return (user_dict)


while in_parametrs != 'Конец ввода':
    in_parametrs = input('Для ввода информации введите 1, "Конец ввода" для выхода из программы')
    if in_parametrs == '1':
        big_word = ''
        for p in param_insert:
            param = input(p)
            if big_word == '':
                big_word = param
            else:
                big_word = big_word + ' ' + param
        words = big_word.split()
        if len(words) == 6:
            print(user_data_get(words[0], words[1], words[2], words[3], words[4], words[5]))




print(user_data_get('Иван', 'Иванов','1999','Зеленоград','ivanov@ianan.ru','999-99-99'))