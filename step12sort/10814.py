import sys
n = int(sys.stdin.readline().rstrip())
d = {}
for i in range(n):
    a,b = map(str, sys.stdin.readline().split())
    print(a,b)
    d.setdefault(a,b)

print(d)
