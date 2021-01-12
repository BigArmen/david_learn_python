def int_func(my_word):
    my_word = str(my_word)
    return my_word[0].upper() + my_word[1:len(my_word)-1].lower()
in_parametrs=''

while in_parametrs != 'F':
    in_parametrs = input('Введите  слова через пробел (целые):')
    words = in_parametrs.split()
    for word in words:
        print(int_func(word))

