param_korteg = ('название', 'цена', 'количество', 'ед')
i_row = 0
in_parametrs = ""
list_rows = []
while in_parametrs != 'Конец ввода':
    in_parametrs = input('Введите инормацию 1, для ввода новой позиции, 2 для просмотра введенных данных, "Конец ввода" для выхода из программы')
    print (f'введен параметр {in_parametrs}')
    if in_parametrs == '1':
        d = {'one': 1}
        for p in param_korteg:
            d[p] = input(p)
        del d['one']
        i_row = i_row + 1
        row_value = [i_row, d]
        list_rows.append(row_value)
        print(d)
        print(row_value)
    elif in_parametrs == '2':
        for p in list_rows:
            print(p)
        w = {}
        a_lists = []
        for k in param_korteg:
            #print(k)
            w_value = ""
            for p in list_rows:
                if w_value == "":
                    w_value = p[1][k]
                else:
                    w_value = w_value + ', ' + p[1][k]
            #print(w_value)
            w = {k: w_value}
            a_lists.append(w)
            #print(w)
        for l in a_lists:
            print(l)








    else:
        print ("Конец программе") if param_korteg == "Конец ввода" else  print ("Конец Программе")






#for p in list_rows:
 #   print(p)
