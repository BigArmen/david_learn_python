n_value = input("Введите число n:")
try:
    nn_value = int(n_value)
    print("Это правильный ввод! Вы ввели число", n_value)
    nn_value =2 * n_value
    nnn_value = 3 * n_value
    print(nn_value)
    print(nnn_value)
    sum_value = int(n_value) + int(nn_value) + int(nnn_value)
    print("Сумма числа вида n + nn + n7nnn",  sum_value)


except ValueError:
    print("Это не правильный ввод. Это не число\n Введеите еще раз, повтроно запустив программу", n_value)

