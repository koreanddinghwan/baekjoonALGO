# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

import sys
n = int(sys.stdin.readline().rstrip())

lst = []
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())

s = set(lst)
lst = list(s)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)