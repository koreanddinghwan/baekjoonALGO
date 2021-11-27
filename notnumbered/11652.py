import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())

lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))

# lst에서 개수세기

count = Counter(lst).most_common()
maxnum = count[0][1] #첫번째 인자의 개수는 항상 최대값일 것임
a = sorted(count, key=lambda x: x[0])

answer = []

for i in a:
    if i[1] != maxnum:
        continue

    answer.append(i)
print(answer[0][0])

