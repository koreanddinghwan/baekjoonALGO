import sys
n = int(sys.stdin.readline().rstrip())

have_lst = list(map(int, sys.stdin.readline().split()))


m = int(sys.stdin.readline().rstrip())
need_lst = list(map(int, sys.stdin.readline().split()))








#입력데이터 전처리과정

#각 데이터를 키값으로, 밸류값에는 개수를 입력
#만약 키값이 있다면, 개수 +1
#만약 키값이 없다면, 키값을 생성
#딕셔너리는 키값없으면 키에러나므로, try~except로
data = {}
for i in have_lst:
    try:
        if data[i]:
            data[i] += 1
    except:
        data.setdefault(i,1)


#출력
answ = []
for i in need_lst:
    try:
        answ.append(str(data[i]))
    except:
        answ.append('0')

print(" ".join(answ))