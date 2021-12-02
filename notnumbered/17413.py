import sys
from collections import deque

s = list(map(str,sys.stdin.readline().rstrip()))




tag = deque()
answer = []
reversestack = deque()
reverseMode = True
for i in s:
    if i == "<":
        tag.append("<")
        while len(reversestack) != 0:
            answer.append(reversestack.popleft())
        answer.append("<")
        reverseMode = False
    elif i == ">":
        tag.append(">")
        answer.append(">")
        reverseMode = True
    elif i == " ":
        if reverseMode == True:
            while len(reversestack) != 0:
                answer.append(reversestack.popleft())
            answer.append(" ")
        else:
            answer.append(" ")
    else:
        if reverseMode == True:
            reversestack.appendleft(i)
        else:
            answer.append(i)

if len(reversestack) != 0:
    while len(reversestack) != 0:
        answer.append(reversestack.popleft())

# print(reversestack)
# print(answer)
print("".join(answer))
