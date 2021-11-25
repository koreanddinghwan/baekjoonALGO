import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
qu = deque()

lst1 = list(map(int, sys.stdin.readline().split()))
lst2 = list(map(int, sys.stdin.readline().split()))

for _ in lst2:
    qu.append(_)



totalcost = 0
min_chker = []

for _ in lst1:
    checker = qu.popleft()
    if len(min_chker) == 0:
        min_chker.append(checker)
    else:
        if min_chker[0] > checker:
            min_chker[0] = checker
    totalcost += min_chker[0] * _

print(totalcost)