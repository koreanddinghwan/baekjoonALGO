#해시함수

import sys
n = int(sys.stdin.readline().rstrip())
key = sys.stdin.readline().rstrip()


r = 31
m = 1234567891

#a부터 z까지 고유번호 생성

alpha = list(map(chr, range(97,123)))

result = 0

for i in range(len(key)): #I:현재 인덱스값
    if key[i] in alpha: #만약 알파벳중에 있으면요
        #알파벳 리스트에서 찾은 key[i]의 인덱스값 + 1 * 31**(i+1)을 result에 더합니다.
        result += (alpha.index(key[i]) + 1) * r**(i)


print(result%m)