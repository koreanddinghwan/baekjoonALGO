from collections import deque
import sys
n,k = map(int, sys.stdin.readline().split())

q = deque()

ans = []

for i in range(1,n+1):
    q.append(i)

for i in range(n):
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())


s = ""
s = s + "<"


for i in range(len(ans) - 1):
    s = s + str(ans[i])
    s = s + ", "

s = s +  str(ans[-1]) + ">"
print(s)