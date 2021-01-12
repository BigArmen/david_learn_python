import math
import itertools


def my_fact(end_number):
    s = 1
    for el in range(1, end_number):
        s= s*el
        yield s


def my_print_iter(my_iter):
    try:
        print(next(my_iter))
    except StopIteration:
        print('End list')


my_iter = my_fact(9)

my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)