import sys

n,m = map(int, sys.stdin.readline().split())

table = {}

for i in range(n):
    site, pw = map(str, sys.stdin.readline().split())
    table.setdefault(site,pw)

for i in range(m):
    s = sys.stdin.readline().rstrip()
    print(table[s])