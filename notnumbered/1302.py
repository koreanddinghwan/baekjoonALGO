# 김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 
# 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

# 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 
# 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

from collections import Counter
import sys


n = int(sys.stdin.readline().rstrip())

#리스트에 넣기 O(N)
name_lst = []
for i in range(n):
    name = sys.stdin.readline().rstrip()
    name_lst.append(name)

#counter생성 O(N)
#갯수대로 정렬되어있음
commoncount = Counter(name_lst).most_common()
# print(commoncount)

#최고값을 가진 상태로, 다음 값이 최고값과 달라지면 stop하는 명령문

max_commoncount = commoncount[0][1]

#이름을 담을 리스트 생성
mostcommon_name = []
mostcommon_name.append(commoncount[0][0])

#첫번째 값과 다른 값부터 시작
for i in range(1, len(commoncount)):

    #개수가 현재 max_commoncount와 같을때만 추가, 다르면 for문 stop
    checker = commoncount[i][1]
    if max_commoncount == checker:
        mostcommon_name.append(commoncount[i][0])
    else:
        break

# print(mostcommon_name)
#사전순으로 가장 앞서는 것만 출력, sort는 최악의 경우 1000^2의 시간복잡도
answer = sorted(mostcommon_name)
print(answer[0])
