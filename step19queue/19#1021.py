from collections import deque
import sys,copy

n,m = map(int, sys.stdin.readline().split())

qu = deque()
for i in range(1,n+1):
    qu.append(i)

#뽑아내려고 하는 수 리스트화
need = list(map(int, sys.stdin.readline().split()))

#2,9,5
#1 -> 23456789101 1번
#9-> 9 101345678 6번
# 4번

#오른쪽으로가든, 왼쪽으로가든 최소회수를 찾아서 count에 더해야한다. n이 50보다 작다. 2개다 해보자
count = 0

for i in need:
    checkcount = []

    count1 = 0
    while True:
        print(qu[0],'오른쪽')
        if qu[0] != i:
            qu.appendleft(qu.pop())
            count1 += 1
            
            
        else:
            break
    print(count1)
    print(qu)
    checkcount.append(count1)

    count2 = 0
    while True:
        print(qu[0],'왼쪽')
        if qu[0] != i:
            qu.append(qu.popleft())
            count2 += 1
        else:
            break
    checkcount.append(count2)



    print(checkcount)
    count += min(checkcount)

print(count)


