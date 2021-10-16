
def prime_list(a):
    sieve = [True] * (a+1)
    sosu_list = []
    checkrange = int((a+1)**0.5)

    for i in range(2,checkrange+1):
        if sieve[i] == True:
            for j in range(i+i,a+1,i):
                sieve[j] = False

    sieve[0] = False
    sieve[1] = False

    
    for index,value in enumerate(sieve):
        if value == True:
            sosu_list.append(index)

    return sosu_list

import sys

n = int(sys.stdin.readline().rstrip())




for s in prime_list(n):
    if n == 1:
        break
    while n % s == 0:
        n = n // s
        print(s)
