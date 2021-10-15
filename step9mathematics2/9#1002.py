

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, sys.stdin.readline().split())
    d = ((x_1-x_2)**2 + (y_1-y_2)**2)**0.5
    
    if x_1 == x_2 and y_1 == y_2 and r_2 == r_1:
        print(-1)
        continue

    if x_1 == x_2 and y_1 == y_2 and r_2 != r_1:
        print(0)
        continue

    if r_2 + r_1 < d or abs(r_2-r_1) > d:
        print(0)

    if abs(r_2-r_1) == d or r_2+r_1 == d:
        print(1)

    if abs(r_2-r_1) < d and r_1+r_2 > d:
        print(2)

    