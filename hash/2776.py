import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    note1 = set(list(map(int, sys.stdin.readline().split())))

    #해시테이블(정수리스트)
    dict = {}
    for i in note1:
        dict.setdefault(i,1)

    m = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().split()))
    for i in note2:
        try:
            if dict[i] == 1:
                print(1)

        except:
            print(0)

