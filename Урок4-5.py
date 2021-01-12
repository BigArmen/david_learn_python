from functools import reduce
import os as myos


my_list = [n for n in range(100, 1001, 1) if n % 2 == 0]
# my_list1 = [ a +b for a in my_list for b in my_list]

sum_all = reduce(lambda x, y: x * y, my_list)

print(sum_all)
