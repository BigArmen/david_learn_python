
in_parametrs=''

while in_parametrs != 'F':

    raschody = input("Введите расходы - ")
    vyruchka = input("введите выручку - ")

    print(f'Расходы {raschody} , Выручка {vyruchka}')
    delta = int(vyruchka) - int(raschody)
    rent = delta / int(vyruchka)
    if delta > 0:
        print(f'Предприятие работает с прибылью {delta}')
        print(f'Предприятие работает с рентабельностью {rent}')
        q_person = input('Введите количество сотрудников - ')
        v_value = delta / int(q_person)
        print(f'Прибыльность на сотрудника {v_value}')
    elif delta < 0:
        print(f'Предприятие работает с убытком {delta}')
    else:
        print('Предприятие работает само для себя ')
    in_parametrs = input('Введите F для окончания программы')












