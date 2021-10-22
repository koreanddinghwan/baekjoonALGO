from collections import deque

import sys


t = int(sys.stdin.readline().rstrip())

dq = deque()
for i in range(t):
    usr_inp = list(sys.stdin.readline().split())
    if usr_inp[0] == 'push_front':
        dq.appendleft(usr_inp[-1])

    if usr_inp[0] == 'push_back':
        dq.append(usr_inp[-1])

    if usr_inp[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    if usr_inp[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    if usr_inp[0] == 'size':
        print(len(dq))

    if usr_inp[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    if usr_inp[0] == 'front':
        if len(dq) == 0:
            print(-1)

        else:
            print(dq[0])

    if usr_inp[0] == 'back':
        if len(dq) == 0:
            print(-1)

        else:
            print(dq[-1])



