import sys
import heapq

#(절대값:원래수) 의 형식으로 튜플을 힙연산한다.
#절대값을 기준으로 힙 리스트를 만든다.  

n = int(sys.stdin.readline().rstrip())
lst = []
lstlen = 0
for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    if data == 0:
        if lstlen == 0:
            print(0)
        else:
            print(heapq.heappop(lst)[1])
            lstlen -= 1
    else:
        heapq.heappush(lst, (abs(data), data))
        lstlen += 1

