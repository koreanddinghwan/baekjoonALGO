import math,sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    
    a = math.factorial(m)//(math.factorial(m-n)*math.factorial(n))
    print(a)