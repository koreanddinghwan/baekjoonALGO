import sys
from collections import deque


class queue():
    def __init__(self):
        self.item = deque()
    
    def push(self, val):
        self.item.append(val)

    def pop(self):
        if len(self.item) != 0:
            return print(self.item.popleft())

        elif len(self.item) == 0:
            return print(-1)

    def size(self):
        return print(len(self.item))

    def empty(self):
        if len(self.item) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(self.item) == 0:
            return print(-1)
        else:
            print(self.item[0])
    def back(self):
        if len(self.item) == 0:
            return print(-1)
        else:
            print(self.item[-1])

s = queue()

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    command = list(map(str,sys.stdin.readline().split()))
    if command[0] == 'push':
        s.push(command[-1])
    elif command[0] == 'pop':
        s.pop()
    elif command[0] == 'size':
        s.size()
    elif command[0] == 'empty':
        s.empty()
    elif command[0] == 'front':
        s.front()
    elif command[0] == 'back':
        s.back()