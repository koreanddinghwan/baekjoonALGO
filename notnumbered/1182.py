import sys

import itertools

n,s = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

#조합구하기
count = 0
for i in range(1,n+1):
    a = list(itertools.combinations(lst,i))
    for _ in a:
        if sum(list(_))  == s:
            count += 1


print(count)
