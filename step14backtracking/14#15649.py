import sys
import itertools


n,m = map(int, sys.stdin.readline().split())


lst = [i for i in range(1,n+1)]

answ = list(itertools.permutations(lst,m))

for i in answ:
    _list = map(str, i)
    print(" ".join(list(_list)))