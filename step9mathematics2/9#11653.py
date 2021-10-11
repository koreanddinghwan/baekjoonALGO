import sys

n = int(sys.stdin.readline().rstrip())
a = n
k = 2
while  a != 1:
    if a % k == 0:
        print(k)
        a = a / k
        continue
    else:
        k = k + 1

    

