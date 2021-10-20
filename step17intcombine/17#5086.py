import sys

while True:
    a,b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    
    if a / b > b / a:
        if a / b % 1 == 0:
            print('multiple')
        else:
            print('neither')



    elif a / b < b / a:
        if b / a % 1 == 0:
            print('factor')
        else:
            print('neither')





    