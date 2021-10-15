# 10000개 이하의 수에 대해 에라토스테네스의 체로 소수를 구한다.(캐싱)
# 여러가지 경우가 가능한 경우를 막기위해, 중간값에서 먼쪽으로 나아간다. 
# 가장먼저 발견되는 경우가 두 소수의 차이가 가장 작은 것이다.



#1. 입력받은 짝수n를 2로 나누어  n/2 부터 탐색을 시작한다.
#2. n/2 이하의 수들 중, 소수x를 발견하면-> n-x도 소수라면->출력

def prime_list(a):
    sieve = [True] * (a+1)

    checkrange = int((a+1)**0.5)

    for i in range(2,checkrange+1):
        if sieve[i] == True:
            for j in range(i+i,a+1,i):
                sieve[j] = False

    sieve[0] = False
    sieve[1] = False

    return sieve

lst_sieve = prime_list(10000)



import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())

    for sieve_index_num in range(int(n/2),0,-1):  #에라토스테네스의 체에서 입력받은 n의 중간값부터 역순으로 접근.
        if lst_sieve[sieve_index_num] == True: #만약 현재 체의 인덱스값이 소수라면
            if lst_sieve[n-sieve_index_num] == True: #만약 n-체의 인덱스값도 소수라면
                print(sieve_index_num, n-sieve_index_num) #순서대로 출력하고 안쪽 for문탈출, 다음값 입력받음
                break
            else:
                continue #다음 sieve_index_num으로 넘어감(-1)

    












