# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 




#에라토스테네스의 체로 246912까지의 소수를 구해보자.
#2n까지의 소수의 개수 - n까지의 소수의 개수하면 n보다 크고 2n보다 작거나 같은 소수의 개수를 구할 수 있다.
#2n까지 에라토스테네스의 체로 소수를 체크하고,
#n초과 2n이하의 범위로 구해내자.




def prime_list(num):
    if num == 1:
        return 1


    sieve = [True] * 2*num  #2*num까지, 2*num개를 소수로 가정한다.

    m = int(2*num ** 0.5)   #2*num의 최대 약수는 제곱근 이하
    for i in range(2,m + 1):   #2부터 m까지 체크
        if sieve[i] == True:   #만약 소수라고 가정되어있으면
            for j in range(i+i, 2*num, i):  #자기 자신을 제외한 자신의 배수들에 대해 소수가 아니라고 판정.
                sieve[j] = False

    prime_cnt = sieve[num+1:].count(True)    #num초과, 끝까지 소수의 개수를 카운트

    return prime_cnt #리턴으로 (소수의개수, 입력값이 소수인지 아닌지를 반환한다.)

import sys


while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break
    
    else:
        print(prime_list(n))



















