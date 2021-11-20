import sys
import itertools


while True:
    a = list(map(int, sys.stdin.readline().split()))

    if a[0] == 0:
        break

    answer = list(itertools.combinations(a[1:],6))
    for i in answer:
        print(" ".join(list(map(str, i))))

    print()