#음계, deepcopy, 깊은복사

import sys, copy
n = list(map(int, sys.stdin.readline().split()))
original_lst = copy.deepcopy(n)

n.sort()
lst_sorted = copy.deepcopy(n)

n.reverse()
lst_reversed = copy.deepcopy(n)


if lst_reversed == original_lst:
    print('descending')

elif lst_sorted == original_lst:
    print('ascending')

else:
    print('mixed')