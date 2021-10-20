class stack() :
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def plus(self):
        return sum(self.items)


import sys
n = int(sys.stdin.readline().rstrip())

cog = stack()

for i in range(n):
    shout = int(sys.stdin.readline().rstrip())
    if shout != 0:
        cog.push(shout)
    if shout == 0:
        cog.pop()


print(cog.plus())