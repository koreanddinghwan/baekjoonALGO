import sys
from collections import deque

#문자열을 리스트로 받아 cursor를 인덱스로, 여기에 insert하는 연산은 시간초과가 발생할 것임.

#문자열을 리스트로 받기
n = list(map(str, sys.stdin.readline().rstrip()))
c = int(sys.stdin.readline().rstrip())
ostack = deque()

for i in n:
    ostack.append(i)

#2중스택으로 구현하고, 
#L이면 pop/append으로 다른 스택에 집어넣기
#D면 다른 스택에 집어넣었던 문자열 다시 넣기
# B면 pop으로 삭제
#P면 다음문자 삽입

#ostack에 원래 문자열들 나열되어있음.
#문자열을 잠시 옮겨놓을 다른 스택 만들기
tempstack = deque()

for _ in range(c):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L': #L일때, 현재 original stack의 마지막 문자를 pop해 tempstack에 넣기
        if len(ostack) != 0:
            tempstack.append(ostack.pop())
        
    elif command[0] == 'D':
        if len(tempstack) != 0:
            ostack.append(tempstack.pop())

    elif command[0] == 'B':
        if len(ostack) != 0:
            ostack.pop()

    elif command[0] == 'P':
        ostack.append(command[1])
        
answerostack = "".join(ostack)
tempstack.reverse()
answertempstack = "".join(tempstack)

print(answerostack + answertempstack)