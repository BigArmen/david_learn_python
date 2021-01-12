import my_functions


my_functions.z_calculate()
in_parametrs = '_'

while in_parametrs != 'Конец ввода':
    in_parametrs = input('Для ввода информации введите 1 , "Конец ввода" для выхода из программы')

    if in_parametrs == '1':
        working_out = '_'
        rate_per_hour = '_'
        prize = '_'
        zp = 0

        FIO = input('Введите ФИО сотрудника -')
        while working_out.isdigit() == False:
            working_out = input('Введите количество отработанных часов - ')
        print(working_out)
        while rate_per_hour.isdigit() == False:
            rate_per_hour = input('Введите стоимость ставки  - ')
        print(rate_per_hour)
        while prize.isdigit() == False:
            prize = input('Введите процент премии  - ')
        print(rate_per_hour)
        zp = my_functions.z_calculate (int(working_out), int(rate_per_hour), int(prize))
        print(f'Сотрудник {FIO}, заработал сумму {zp}')
