import sys
n = int(sys.stdin.readline().rstrip())

dict = {}

for i in range(n):
    a = sys.stdin.readline().rstrip()
    try:
        dict[a] += 1

    except:
        dict.setdefault(a,1)


for i in range(n-1):
    a = sys.stdin.readline().rstrip()
    dict[a] -= 1

for i in dict.keys():
    if dict[i] != 0:
        print(i)
