import sys

n = int(sys.stdin.readline().rstrip())

input_lst = list(map(int, sys.stdin.readline().split()))

sorted_input = sorted(input_lst)


table = {}

for i in sorted_input:
    table.setdefault(i,i)

m = int(sys.stdin.readline().rstrip())
check_lst = list(map(int, sys.stdin.readline().split()))

for i in check_lst:
    try:
        if table[i] != 0:
            print(1)
    except:
        print(0)



