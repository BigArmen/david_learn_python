mount_list = ['зима', 'зима', 'весна','весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']

nmoumt_value = input('Введите номер месяца - ')

if nmoumt_value.isnumeric():
    if int(nmoumt_value) < 13:
        print(mount_list[int(nmoumt_value)-1])
    else:
        print('Номер месяца введен не коррктно')
else:
    print("Необходимо ввести число")



