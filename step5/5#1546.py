import sys
n = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().split()))

# 새로운 점수 입력할 리스트
new_score = []

# 각 입력점수에 대해서
for i in score:
    # 계산값을 새 리스트에 추가
    new_score.append(i/max(score)*100)

# 새 리스트의 평균
print(sum(new_score)/n)
    