import sys

an, bn = map(int, sys.stdin.readline().split())

a = []
a.append(list(map(int, sys.stdin.readline().split())))


b = []

b.append(list(map(int, sys.stdin.readline().split()))) 



a_set = set(a[0])
b_set = set(b[0])
intersect = a_set - b_set
intersect = list(a_set-b_set)
intersect.sort()
intersection = list(map(str,intersect))


if len(a_set - b_set) == 0:
    print(len(a_set - b_set))
else:
    print(len(a_set - b_set))
    print(" ".join(intersection))