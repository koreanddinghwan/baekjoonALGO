import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())


#산술평균
sum = 0


#숫자리스트
num_list = []

#4최대값,최소값비교
minnum = None
maxnum = None

for i in range(n): #홀수개수입력
    num = int(sys.stdin.readline().rstrip())
    #산술평균
    sum += num
    num_list.append(num)

    #4최대값,최소값비교
    if minnum == None:
        minnum = num
    else:
        if minnum > num:
            minnum = num
    
    if maxnum == None:
        maxnum = num
    else:
        if maxnum < num:
            maxnum = num
    




#1산술평균
print("{}".format(round(sum/n)))

#2중앙값
num_list.sort()
print(num_list[n//2])

#3최빈값
numbers_cnt = Counter(num_list) #각 수별 카운팅

#카운팅된 것들 중 최빈값은 맨 앞에 올거임
maxmod_cnt = numbers_cnt.most_common()[0][1] 
# print(maxmod_cnt)
#최빈값 여러개일수도있으므로 최빈값들 넣을 리스트

maxmodcnt_lst = []
for i in numbers_cnt.most_common():
    if i[1] == 1:
        maxmodcnt_lst.append(i)
    elif i[1] == maxmod_cnt:
        maxmodcnt_lst.append(i)
    else:
        break

if len(maxmodcnt_lst) == 1:
    print(maxmodcnt_lst[0][0])
else:
    print(maxmodcnt_lst[1][0])


#4범위
print(abs(maxnum - minnum))