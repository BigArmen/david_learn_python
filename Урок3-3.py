def my_func(num1, num2, num3):
    a = [num1, num2, num3]
    max1 = get_max(a)
    a.remove(max1)
    max2 = get_max(a)
    return max1 + max2


def get_max(n_collection):
    n_max = 0
    for n in n_collection:
        if n >= n_max:
            n_max = n
    return n_max


print(my_func(78, 166, 100))
