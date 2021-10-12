import sys

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == a[1] == a[2] == 0:
        break
    a.sort()
    max_A = a.pop()
    if max_A**2 == a[0]**2 + a[1]**2:
        print("right")
    else:
        print('wrong')
        
    