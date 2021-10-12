import sys
m, n = map(int, sys.stdin.readline().split())

#에라토스테네스의 체로 소수검증하기.
def isprime(a):
    if a == 1:
        return False   #1인경우, 에라토스테네스의 체 적용 제외한다.
    
    else:
        #2부터 입력 a의 제곱근까지의 수들 중에서 2부터 i에 할당한다.
        for i in range(2, int(a**(1/2)) + 1): 

            #만약 i로 나눠떨어진다면, 1을 제외한 수들 중 약수가 있다는 의미이므로 소수가 아니다.
            if a % i == 0:
                return False 
    
        #만약 소수이면 True를 리턴한다.
        return True 
    


for i in range(m,n+1):
    if isprime(i):
        print(i)