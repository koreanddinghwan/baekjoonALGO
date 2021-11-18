import sys
from collections import Counter

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    dict = {}
    lst =[]
    for i in range(n):

        name, case = map(str, sys.stdin.readline().split())
        lst.append(case)

    a = Counter(lst).most_common()
    totalnum = 1
    for i in range(len(a)):
        totalnum *= a[i][1] + 1
    print(totalnum-1)


#
#2,2,1 ->  4*4*2 -1?
# 2,1 ->  (2^2-1)+2^1 - 1?
# 3 -> 