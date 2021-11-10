import sys

n = sys.stdin.readline().rstrip()


lst = []
for i in range(int(n)):
    s = list(sys.stdin.readline().rstrip())
    s.sort()
    if s not in lst:
        lst.append(s)


print(len(lst))







