import sys
from math import gcd


n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    lst.append(data)

sorteddata = sorted(lst)



dife = []
for i in range(len(sorteddata[:-1])):
    dife.append(sorteddata[i+1]-sorteddata[i])

gcdlst = []
gcdlst.append(dife[0])
for i in dife:
    check = gcd(i,gcdlst[0])
    if check <= gcdlst[0]:
        gcdlst[0] = check
    else:
        continue

count = 0
for i in dife:
    count += i // gcdlst[0] - 1

print(count)