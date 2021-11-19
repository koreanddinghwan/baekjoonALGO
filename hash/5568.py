import sys
import itertools

n = int(sys.stdin.readline().rstrip())

k = int(sys.stdin.readline().rstrip())

dict = {}
num_lst = []
for i in range(n):
    num_lst.append(sys.stdin.readline().rstrip())


_ = set(itertools.permutations(num_lst,k))

for i in _:
    if k == 2:
        dict.setdefault(i[0]+i[1],0)
    elif k == 3:
        dict.setdefault(i[0]+i[1]+i[2],0)
    else:
        dict.setdefault(i[0]+i[1]+i[2]+i[3],0)
print(len(dict))
