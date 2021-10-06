# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.


# 문제 정의
# 중복문자열 제거, 각 문자의 rfind과 find의 인덱스값이 같으면 그룹단어
# 다르면 그룹단어가 아님


# n입력
import sys

cycle = int(sys.stdin.readline().rstrip())
count = 0
for i in range(cycle):
    
    # 각 문자 입력
    n = sys.stdin.readline().rstrip()
    checker = []
    # 문자열 안의 각 문자에 대해
    for char in n:
        # 만약 checker에 char이 있다면
        if char in checker:
            # checker의 마지막문자가 char와 다르다면, 즉 연속되지 않으면 for문 종료하고 바깥for문인 cycle로 돌아가 다음 문자 입력받는다.
            if checker[-1] != char:
                break
        # 만약 checker에 char가 없으면 checker에 추가.
        else:
            checker.append(char)
    # for else문은 for문이 break로 종료되지 않았을 경우의 실행코드를 담는다.
    else:
        count += 1

print(count)