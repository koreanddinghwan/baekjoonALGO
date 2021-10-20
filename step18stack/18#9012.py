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


def parchecker(expr) :
    s = stack()

    for char in expr:
        if char == '(':
            s.push(char)
        
        elif char == ')':
            if s.isempty():
                return print("NO")
            else:
                s.pop()

    if s.isempty():
        return print('YES')
    else:
        return print('NO')
for i in range(n):
    exp = sys.stdin.readline().rstrip()
    parchecker(exp)
