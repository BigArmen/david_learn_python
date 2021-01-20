n_value = input("Введите число n:")
max_value = 0
# i_value = 1


try:
    n_value = int(n_value)

    while n_value > 0:
        get_value = int(n_value % 10)
        print('Цифра ', get_value)
        if get_value > max_value:
            max_value = get_value
            print('Новое максимальное значеие цифры', max_value)
        n_value = int((n_value - get_value) / 10)
        print('Новое значение число  для поиска цифры', n_value)
        i_value = n_value // 10
        print('Новое значение параметра продолжения While', i_value)

    print('Максимальная Цифра', max_value)

except ValueError:
    print("Это не правильный ввод. Это не число\n Введеите еще раз, повтроно запустив программу", n_value)
