#  2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다. 
#원래 수 a * b / 최대공약수 = 최소공배수 공식이 성립한다.


import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    if a>b:
        bn = a
        sn = b
    elif a < b:
        bn = b
        sn = a

    else:
        bn = a
        sn = b

    while True:
        r = bn % sn
        if r == 0:
            break
        bn = sn
        sn = r
    
    print(int(a*b/sn))

