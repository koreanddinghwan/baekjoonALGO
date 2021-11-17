import sys
n = int(sys.stdin.readline().rstrip())

d = {}
for i in range(n):
    name, move = map(str, sys.stdin.readline().split())
    if move == "leave":
        d.__delitem__(name)

    elif move == "enter":
        d.setdefault(name)


answe = d.keys()
lst = []
for i in answe:
    lst.append(i)


a = sorted(lst)
a.reverse()
for i in a:
    print(i)