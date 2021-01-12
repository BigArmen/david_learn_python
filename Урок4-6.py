import itertools

def my_iter_f ( start_number, end_number):
    for el in itertools.count(start_number):
        if el > end_number:
            break
        else:
            yield el

def my_iter_fcycle ( objekt_cycle, end_number):
    с = 0
    for el in itertools.cycle(objekt_cycle):
        if с > end_number:
            break
        else:
            с += 1
            yield el


def my_print_iter (my_iter):
    try:
        print(next(my_iter))
    except StopIteration:
        print('End list')



#my_iter = itertools.count(start=0, step=1)
my_iter =[]
my_iter = my_iter_f( 10, 16)


my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)
my_print_iter(my_iter)



#progr_lang = ["python", "java", "perl", "javascript"]
progr_lang = ["python", "java"]
#iter = itertools.cycle(progr_lang)
iter = my_iter_fcycle (progr_lang, 9)

my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)
my_print_iter(iter)