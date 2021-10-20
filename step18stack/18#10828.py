import sys

n = int(sys.stdin.readline().rstrip())

class stack() :

    def __init__(self): 
        self.items = [] #stack()클래스의객체생성함수

    def push(self,value):
        self.items.append(value) #추가

    def pop(self):
        try:
            return print(self.items.pop()) #있으면 리턴하고 제거
        except:
            print(-1) #없으면 -1

    def size(self):
        return print(len(self.items)) #길이 리턴

    def top(self):
        try:
            print(self.items[-1]) #마지막값리턴
        except:
            print(-1)


    def isempty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)




opstack = stack()

for i in range(n):
    operation = sys.stdin.readline().split()
    
    if operation[0] == "push":
        opstack.push(operation[-1])

    if operation[0] == "pop":
        opstack.pop()
    if operation[0] == "size":
        opstack.size()
    if operation[0] == "top":
        opstack.top()
    if operation[0] == "empty":
        opstack.isempty()





