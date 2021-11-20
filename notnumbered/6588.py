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

lst_sieve = prime_list(1000000)


import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    for sieve_i in range(len(lst_sieve[:n//2+1])):
        if lst_sieve[sieve_i] == True:
            if lst_sieve[n-sieve_i] == True:
                a = sieve_i
                b = n -sieve_i
                break

    print("{} = {} + {}".format(n,a,b))

    

# t = int(sys.stdin.readline().rstrip())

# for i in range(t):
#     n = int(sys.stdin.readline().rstrip())

#     for sieve_index_num in range(int(n/2),0,-1):  #에라토스테네스의 체에서 입력받은 n의 중간값부터 역순으로 접근.
#         if lst_sieve[sieve_index_num] == True: #만약 현재 체의 인덱스값이 소수라면
#             if lst_sieve[n-sieve_index_num] == True: #만약 n-체의 인덱스값도 소수라면
#                 print(sieve_index_num, n-sieve_index_num) #순서대로 출력하고 안쪽 for문탈출, 다음값 입력받음
#                 break
#             else:
#                 continue #다음 sieve_index_num으로 넘어감(-1)