from collections import deque
import sys

card_dummy = deque()

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    card_dummy.append(i)

for i in range(n-1):
    card_dummy.popleft()
    card_dummy.append(card_dummy.popleft())

print(card_dummy.pop())


