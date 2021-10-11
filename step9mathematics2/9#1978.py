import sys

n = int(sys.stdin.readline().rstrip())

k = list(map(int, sys.stdin.readline().split()))

sosu = 0
for i in k:
    if i == 1:
        continue
    f = 1
    cnt = 0
    while f*f <= i:
        if f != 1 and i % f == 0:
            cnt += 1
        
        
        f += 1
        
    if cnt == 0:
        sosu += 1


print(sosu)