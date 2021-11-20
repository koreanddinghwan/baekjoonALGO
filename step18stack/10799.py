import sys
from collections import deque

stack = deque()



data = sys.stdin.readline().rstrip()
count = 0
for i in range(len(data)):
    # 여는괄호가 들어오는 경우
    #스택에 일단 추가
    if data[i] == '(':
        stack.append('(')

    # 닫는 괄호일떄 
    if data[i] == ')':
        # 바로앞이 여는괄호인 경우, 스택에 있는 여는괄호의 개수만큼 총 카운트 추가
        if data[i-1] == '(':
            stack.pop()
            count += len(stack)

        else:
            # 바로앞이 닫는괄호였던 경우, 스택에서 하나빼고, 카운트만 하나 추가
            stack.pop()
            count += 1

print(count)




