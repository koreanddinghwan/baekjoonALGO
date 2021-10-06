# 문제 정의
# 3번의 입력을 받아 곱한 수가 0부터 9까지 각각 몇번쓰였는지 한줄씩 수를 출력한다.

# 풀이
# 3개의 수를 입력받는다.
# 입력받은 수의 곱을 계산한다.
# 리스트형태로 바꾼다.
# 1부터 10까지 result리스트에 각각 개수를 추가한다.

import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

multipled = a * b * c

mul_lst = list(map(int, str(multipled)))

result = []
for i in range(10):
    result.append(mul_lst.count(i))
    
for i in result:
    print(i)