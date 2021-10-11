import sys

m = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())

sosu = []

for i in range(m,n+1):
    if i == 1:
        continue
    
    k = 1
    cnt = 0
    
    while k*k <= i:
        if k != 1 and i % k == 0:
            cnt += 1
            
        k += 1
        
    if cnt == 0:
        sosu.append(i)


if sosu:
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)



