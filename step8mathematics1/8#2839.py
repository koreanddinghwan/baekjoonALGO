import sys

n = int(sys.stdin.readline().rstrip())

mok = n // 5
namuji = n % 5

if namuji == 0:
    print(mok)

elif namuji  == 1 and mok -1 >= 0:
    mok = mok - 1 + 2
    print(mok)
    
elif namuji  == 2 and mok - 2 >= 0:
    mok = mok - 2 + 4
    print(mok)
    
elif namuji  == 3:
    mok = mok + 1
    print(mok)
    
elif namuji  == 4 and mok - 1 >= 0:
    mok = mok - 1 + 3
    print(mok)

else:
    print(-1)
