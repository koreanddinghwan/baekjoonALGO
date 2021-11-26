import sys

class myset:
    def __init__(self):
        self.item = []

    def add(self,value):
        if value in self.item:
            pass
        else:
            self.item.append(value)

    def remove(self,value):
        if value not in self.item:
            pass
        else:
            self.item.remove(value)

    def check(self,value):
        if value in self.item:
            return 1
        else:
            return 0


    def toggle(self,value):
        if value in self.item:
            self.item.remove(value)
        else:
            self.item.append(value)

    def all(self):
        self.item = [i for i in range(0,21)]

    def empty(self):
        self.item = []


case = int(sys.stdin.readline().rstrip())
S = myset()

for i in range(case):
    cval = list(map(str, sys.stdin.readline().split()))
    if cval[0] == 'add':
        S.add(int(cval[1]))
    elif cval[0] == 'remove':
        S.remove(int(cval[1]))

    elif cval[0] == 'check':
        print(S.check(int(cval[1])))

    elif cval[0] == 'toggle':
        S.toggle(int(cval[1]))

    elif cval[0] == 'all':
        S.all()
    
    elif cval[0] == 'empty':
        S.empty()

