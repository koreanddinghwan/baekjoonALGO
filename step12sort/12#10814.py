import sys
n = int(sys.stdin.readline().rstrip())
lst = []
for i in range(n):
    age, name = map(str,sys.stdin.readline().split())
    lst.append([int(age),name])


answ = sorted(lst, key = lambda x: x[0])
for i in answ:
    print(i[0], i[1])