import sys
n = int(sys.stdin.readline().rstrip())


numlst = [0] * 10001
for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    numlst[data] += 1

for i in range(1,10001):
    if numlst[i] != 0:
        for a in range(numlst[i]):
            print(i)



