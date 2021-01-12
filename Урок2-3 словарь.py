mount_dict = dict(k1='зима', k2='зима', k3='весна', k4='весна', k5='весна', k6='лето', k7='лето', k8='лето', k9='осень', k10='осень', k11='осень', k12='зима')


nmoumt_value = input('Введите номер месяца - ')

if nmoumt_value.isnumeric():
    if int(nmoumt_value) < 13:
        print(mount_dict.get('k' + nmoumt_value))
    else:
        print('Номер месяца введен не коррктно')
else:
    print("Необходимо ввести число")