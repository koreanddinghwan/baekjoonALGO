import sys

t,n = map(int,sys.stdin.readline().split())

pocketmon = {}
pocketmonlst = []

for i in range(t):
    data = sys.stdin.readline().rstrip()
    pocketmon.setdefault(data,i+1)
    pocketmonlst.append(data)

for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a.isalpha():
        print(pocketmon[a])
    elif a.isnumeric():
        print(pocketmonlst[int(a) -1])







