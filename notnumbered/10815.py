import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())


b = list(map(int, sys.stdin.readline().split()))

table = {}
for i in a:
    table.setdefault(i,0)

answer = []
for i in b:
    try:
        if table[i] == 0:
            answer.append('1')

    except:
        answer.append('0')


print(" ".join(answer))