import sys


m,n = map(int, sys.stdin.readline().split())

#수 정렬
big_num = m
small_num = n
if n > m:
    big_num = n
    small_num = m



# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다. 
#원래 수 a * b / 최대공약수 = 최소공배수 공식이 성립한다.

#최대공약수 계산
def uclid(a,b):
    r = a % b 

    #나머지가 0이라면 재귀함수호출 종료, 둘 중 작은수가 약수이므로 small리턴
    if r == 0:
        return b

    return uclid(b,r)


#최소공배수 계산
def minmultiple(a,b):
    r = a % b 

    #나머지가 0이라면 재귀함수호출 종료, b가 최대공약수이므로 원래 수 / 최대공약수 = 최소공배수
    if r == 0:
        return int(big_num * small_num / b)

    return minmultiple(b,r)
    


print(uclid(big_num,small_num))
print(minmultiple(big_num,small_num))