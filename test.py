import sys

n = list(map(int,sys.stdin.readline().rstrip().split(";")))

n.sort()
n.reverse()

for i in n:
    print("{0:>9,}".format(i))

