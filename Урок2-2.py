sample_list = []
el_count = 0

while el_count < 5:
    sample_list.append(input('Введите новый элемент списка, '))
    el_count = el_count + 1
for s in sample_list:
    print(s, type(s))

n_count = len(sample_list)
print (len(sample_list))


for i in range(0, n_count, 2):
    print(i)
    if i + 1 < n_count:
        m1_value = sample_list[i]
        m2_value = sample_list[i+1]
        sample_list[i] = m2_value
        sample_list[i + 1] = m1_value


for s in sample_list:
    print(s, type(s))


