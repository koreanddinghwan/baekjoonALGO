# 입력
# 첫 줄에 알파벳 대소문자 및 숫자, 그리고 공백으로 구성된 문자열이 들어온다. 이 문자열의 길이는 $10\ 000$자 이하다.

# 문자열의 맨 앞이나 맨 뒤는 공백이 아님이 보장된다.

# 출력
# 문자열 안에 $D2$나 $d2$가 들어있다면 D2를 출력한다. 두 글자는 반드시 붙어있어야 하며, $D$/$d$와 $2$ 사이에 공백이 있어도 안 된다.

# 만약 문자열 안에 해당 문자가 없다면 unrated를 출력한다.




# import sys

# n = sys.stdin.readline().split()
# print(n)
# for i in n:
#     print(i)
#     if i == 'd2' or 'D2':
#         print('D2')
#         break
# else:
#     print('unrated')




# 아카라카 펠린드롬

import sys, copy
from collections import deque


n = sys.stdin.readline().rstrip()

a = deque()

for i in n:
    a.append(i)

print(a)

#덱에 짝수개수가 들어왔을때
if len(a) % 2 == 0:
    



#덱에 홀수개수가 들어왔을때