import sys

n = int(sys.stdin.readline().rstrip())


a = list(map(int, sys.stdin.readline().split()))

b = list(map(int, sys.stdin.readline().split()))



sorteda = sorted(a)

sortedb = sorted(b)
sortedb.reverse()


total = 0


for i in range(len(sorteda)):
    total += sorteda[i] * sortedb[i]

print(total)