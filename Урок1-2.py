second_value = input("Введите время в секундах:")

#Прверяем правильность ввода значения числа
try:
    second_value = int(second_value)
    print("Это правильный ввод! Вы ввели число", second_value)
except ValueError:
    print("Это не правильный ввод. Это не число\n Введеите еще раз, повтроно запустив программу", second_value)
#Прверяем правильность величины ввода
hh_value = second_value // 3600
print("Количество часов:", hh_value)

ms_value = second_value % 3600

print("Количество минут и секунд:", ms_value)

mm_value = ms_value // 60
print("Количество минут", mm_value)

ss_value = ms_value % 60
print("Количество секунд:", ss_value)

if mm_value < 10:
    mm_value = str(mm_value)
    mm_value= "0" + mm_value
else:
    mm_value = str(mm_value)

print("Количество минут, форматированное", mm_value)

if ss_value < 10:
    ss_value = str(ss_value)
    ss_value= "0" + ss_value
else:
    ss_value = str(ss_value)

print("Количество секунд, форматированное", ss_value)



print(f'Введенная величиеа соответсвует указанной в соответсвующий формат значение {hh_value}:{mm_value}:{ss_value}')
