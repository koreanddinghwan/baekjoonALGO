import sys

# zero_c = 0
# one_c = 0
# def fibo(n):
#     global zero_c, one_c
#     if n == 1:
#         one_c += 1
#         return 1

#     elif n == 0:
#         zero_c += 1
#         return 0
#     else:
#         return fibo(n-1) + fibo(n-2)

# n = int(sys.stdin.readline().rstrip())
# fibo(n)
# print(zero_c, one_c)

##캐싱을 사용해서,분리시에 fibo(0)이 호출되면 0이 호출되는 횟수가 증가, fibo(1)은 1이 호출번수 증가
#이 호출되는 횟수가 현재 피보나치 수열의 특징을 띄고있음.
#0 -> 1 0
#1 -> 0 1
#2 -> 1 1
#3 -> 1 2
#---------
# 1 0 1 1 2 3 5
#이거를 메모이제이션을 이용해 피보나치 수열을 만들자.
#입력으로 0이 들어오면 1,0 즉 F(0), F(0+1)을 출력한다.


def fibo(n):
    if n == 0:
        return F[0]
    elif n == 1:
        return F[1]
    else:
        if F[n] == -1:
            F[n] = fibo(n-1) + fibo(n-2)
        return F[n]

import sys
t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    if n >= 2:
        F = [1,0] + [-1]*(n-1)
    else:
        F = [1,0]
    fibo(n)

    if n == 0:
        print(F[0], F[-1])
    else:
        print(F[-1], F[-1] + F[-2])



