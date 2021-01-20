n_value = input("Введите число n:")
try:
    n_value = int(n_value)
    print("Это правильный ввод! Вы ввели число", n_value)
    nn_value = 2 * str(n_value)
    nnn_value = 3 * str(n_value)
    print(f'число тип n {n_value}')
    print(f'число тип nn {nn_value}')
    print(f'число тип nnn {nnn_value}')
    sum_value = int(n_value) + int(nn_value) + int(nnn_value)
    print("Сумма чисел n + nn + nnn",  sum_value)


except ValueError:
    print("Это не правильный ввод. Это не число\n Введеите еще раз, повтроно запустив программу", n_value)

