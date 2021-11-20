import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

bufer = deque()

while True:
    input = int(sys.stdin.readline().strip())
    if input == -1:
        break

    elif input == 0:
        bufer.popleft()

    else:
        #버퍼가 꽉 찬 상태의경우-> 무시
        if len(bufer) == n:
            continue

        else:
            bufer.append(str(input))


if len(bufer) == 0:
    print('empty')
else:
    print(" ".join(bufer))

