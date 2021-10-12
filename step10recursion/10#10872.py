# <!-- 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오. -->


# 문제정의

# 팩토리얼 : n*(n-1)*(n-2)*(n-3).....*1


import sys

n = int(sys.stdin.readline().rstrip())

def factorial(m):
    
    if m == 1:  #|인풋이 1일때는 바로 1로 출력된다.
        return m
    elif m == 0: #인풋이 0일때는 직접입력될때밖에없다. 1에서 바로 m이 리턴되기때문이다.
        return 1
    
    return m * factorial(m-1) #m이 1도아니고 0도 아닌 경우에는 현재 입력된 m에 factorial(m-1) 을 곱해 factorial(m-1)이 1이면 m-1(1)이 곱해지면서 재귀가끝나도록한다.


print(factorial(n))