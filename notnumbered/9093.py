import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

#n
for i in range(n):
    #텍스트를 문자열로 입력받는다.
    text = sys.stdin.readline().rstrip()

    answer = []
    stack = deque()
    textcount = 0
    for i in range(len(text)):
        if text[i] == " ": #공백이면 모두 pop해서출력
            for i in range(textcount):
                answer.append(stack.pop())
            textcount = 0 #초기화
            answer.append(" ")#공백추가
        else:
            stack.append(text[i]) #공백아니면 추가
            textcount += 1

    #남은거 출력
    for i in range(textcount):
        answer.append(stack.pop())

    print("".join(answer))


        

