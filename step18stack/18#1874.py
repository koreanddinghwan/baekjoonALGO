class stack() :
    def __init__(self): 
        self.items = [] #stack()클래스의객체생성함수

    def push(self,value):
        self.items.append(value) #추가

    def pop(self):
        try:
            return self.items.pop() #있으면 제거하고 리턴
        except:
            return print('error')

    def size(self):
        return len(self.items) #길이 리턴

    def top(self):
        try:
            return self.items[-1] #마지막값리턴
        except:
            return print('error')

    def isempty(self):
        return len(self.items) == 0

import sys

n = int(sys.stdin.readline().rstrip())
inpdata = []

for i in range(n): #인풋 데이터 입력
    inpdata.append(int(sys.stdin.readline().rstrip()))


stackcnt = 1 #현재까지 더하기 연산 몇 번 했는가
result = stack() #연산결과를 저장할 스택
operator = [] #연산자 저장할 리스트
status = True #오류체크

for i in inpdata:  #인풋으로 들어온 각 데이터를 하나씩 입력
    ##연산자 더하는 파트
    while stackcnt <= i: #더하기 연산을 i와 같아질때까지 한다.
        result.push(stackcnt) #할때마다 stackcnt를 result에 push, stackcnt를 +1씩, 연산자에 +를 추가
        stackcnt += 1
        operator.append('+')

    ##연산결과를 리턴하는 파트
    if result.top() == i: #만약 연산결과 스택의 최상부값이 inpdata와 같다면, 그냥 pop하고 '-'연산자 추가
        result.pop()
        operator.append('-')

    else:
        status = False #만일 더하기연산을 했음에도 스택 최상단값과 리턴해야하는 i값이 다른경우, 잘못된 입력이란걸 확인할 status를 False로

if status == False: #만약 status가 False라면 no출력하고 끝내기
    print('NO')

else:
    for i in operator:
        print(i)
    

    











