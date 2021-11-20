import sys

n = int(sys.stdin.readline().rstrip())

lst = list(map(int, sys.stdin.readline().split()))

setted = set(lst)

a = list(setted)

b = sorted(a)

print(" ".join(list(map(str,b))))