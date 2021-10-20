# 이항계수
# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))


# (n_k) = n!/(k!)*(n-k)!


import sys

n,k = map(int, sys.stdin.readline().split())

n_factorial = 1
for i in range(n):
    n_factorial = n_factorial * (i+1)

def factorial(a):
    a_factorial = 1
    for i in range(a):
        a_factorial = a_factorial * (i+1)

    return a_factorial


print(int(factorial(n)/(factorial(k)*factorial(n-k))))
