import sys
m,n = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))


b = set(map(int, sys.stdin.readline().split()))

inter = set.intersection(a,b)
num_a = len(set.difference(a,inter))
num_b = len(set.difference(b,inter))
print(num_a + num_b)