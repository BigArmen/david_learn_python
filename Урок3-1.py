def my_division(number1, number2=0):
    if number2 == 0:
        return "Деление на ноль, введите не нулевое значение"
    else:
        return number1/number2

in_parametrs =""

while in_parametrs != 'Конец ввода':
    in_parametrs = input('Введите два числа через пробел (целые):')
    numbers = in_parametrs.split()
    if len(numbers) < 3:

               if numbers[0].isnumeric() and numbers[1].isnumeric():
                   num1 = int(numbers[0])
                   num2 = int(numbers[1])
                   print(my_division(num1, num2))
               else:
                   print("Введены не числовые значения")