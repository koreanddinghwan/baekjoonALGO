import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())


count = 0
for i in range(n):
    data = sys.stdin.readline().rstrip()
    stack = deque()
    
    for s in data:
        if len(stack) == 0:
            stack.append(s)

        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

    if len(stack) == 0:
        count += 1

print(count)