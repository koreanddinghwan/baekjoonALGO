import sys
from collections import deque


opener = '(['
closer = ')]'

dict = {'(':')', '[':']'}
while True:
    input = sys.stdin.readline().rstrip()
    if input == '.':
        break
    status = True
    stack = deque()
    for i in input:
        #열리는 괄호는 스택에 추가
        if i in opener:
            stack.append(i)
        
        #닫히는 괄호라면
        elif i in closer:
            
            if len(stack) == 0:
                status = False
                break
            #만약 스택의 마지막값이 닫히는 괄호의 여는괄호라면
            elif dict[stack.pop()] != i:
                status = False
                break
            
    #단어체크가 완료되고, 스택에 값이 남아있다면
    if len(stack) != 0:
        status = False

    if status == False:
        print('no')
    else:
        print('yes')





