in_parametrs = ''
num = "{:{align}{width}.{precision}f}"
while in_parametrs != 'F':

    a = int(input("Введите результат первого дня - "))
    b = int(input("введите общий километраж - "))

    day = 0
    while a < b:
        day = day + 1
        if day == 1:
            a = a
        else:
            a = a * 1.1
        #print(num.format(a, align='<', width=8, precision=2))
        aa = num.format(a, align='<', width=8, precision=2)
        print(f'{day} день пройдено {aa}')
    print(f'Потребовалось {day} дней')

    in_parametrs = input('Введите F для окончания программы')
