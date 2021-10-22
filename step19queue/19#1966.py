import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


priodeq = deque()

for i in range(t):
    doc_num, wheredoc = map(int, sys.stdin.readline().split())

    prior = list(map(int, sys.stdin.readline().split()))
    for i in prior:
        priodeq.append(i)

    for i in range(len(priodeq)):
        if priodeq[i] < max(priodeq):
            priodeq.append(priodeq.popleft())

        elif priodeq[i] == max(priodeq):
            print(i,priodeq[i])

    
