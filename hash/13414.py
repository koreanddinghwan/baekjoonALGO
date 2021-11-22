import sys

k,l =map(int, sys.stdin.readline().split())

num = []
for _ in range(l):
    num.append(str(sys.stdin.readline().rstrip()))


h = {}
for i in range(len(num)):
    try:
        h[num[i]]
        del h[num[i]]
        h.setdefault(num[i], i)
    except:
        h.setdefault(num[i], i)


count = 0
for v in h:
    print(v)
    count += 1
    if count == k:
        break