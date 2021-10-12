# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 
# 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 문제 정의
# 입력된 숫자보다 작은 수의 for문을 돌려야한다. 
# 각 자리 수 + 수 = n 인 숫자를 찾아야하낟.
# for문에서 내부 if문에서 만약 걸리면 print하고 break로 for문 탈출
# 안걸리면 for~else로 가서 print(0)하고 종료




import sys

n = int(sys.stdin.readline().rstrip())


for i in range(1,n+1):
    a = list(map(int,str(i)))
    if i + sum(a) == n:
        print(i)
        break
else:
    print(0)
