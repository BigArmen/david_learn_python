def my_division(number1, number2=0):
    if number2 == 0:
        return "Деление на ноль, введите не нулевое значение"
    else:
        return number1 / number2


in_parametrs = ""

big_summ = 0


def my_summ(numbers, big_summ):
    msum = 0
    for number in numbers:
        if number == 'F':
            big_summ = big_summ + msum
            print(big_summ)
            return 'F'

        else:
            msum = msum + int(number)
    return msum


while in_parametrs != 'F':
    in_parametrs = input('Введите  числа через пробел (целые):')
    numbers = in_parametrs.split()
    s = my_summ(numbers, big_summ)
    if s == 'F':

        in_parametrs = 'F'
    else:
        big_summ = big_summ + s
        print(big_summ)
