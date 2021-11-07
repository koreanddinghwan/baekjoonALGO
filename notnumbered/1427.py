import sys

n = sys.stdin.readline().rstrip()

lst = list(map(int, n))
lst.sort()
lst.reverse()
print("".join(str(i) for i in lst))