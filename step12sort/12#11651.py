import sys

n = int(sys.stdin.readline().rstrip())


lst = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())

    lst.append([x,y])


a = sorted(lst, key = lambda x:x[0])
b = sorted(a, key= lambda x:x[1])
for i in b:
    print(i[0], i[1])