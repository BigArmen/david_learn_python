my_list = [7, 5, 3, 3, 2]

reyting_value = input('Введите рейтинг - ')

if reyting_value.isnumeric():
    w_order = 0
    for w in my_list:
        w_order = w_order + 1
        reyting_value = int(reyting_value)
        if reyting_value >= w:
            my_list.insert(w_order-1, reyting_value)
            print(w)
            break

else:
    print("Необходимо ввести число")

for w in my_list:
    print(w)
