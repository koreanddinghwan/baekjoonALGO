# 문제 정의

# 수 10개 입력받고 각각 42로 나눈 나머지를 리스트에 추가한다.
result = []
for i in range(10):
    n = int(input())
    result.append(n/42)


a = set(result)

for i in a:
    print()