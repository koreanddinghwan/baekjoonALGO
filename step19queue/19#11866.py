import sys


class Queue():
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front_index == len(self.items):
            print('queue empty')
            return None
        else:
            returnvalue = self.items[self.front_index]
            self.front_index += 1
            return returnvalue

    def front(self):
        if self.front_index == len(self.items):
            print('queue empty')
        else:
            returnvalue = self.items[self.front_index]
            return returnvalue




def joseph(n,k):
    josephuslst = Queue() #큐 초기화
    result = []
    for i in range(1,n+1):
        josephuslst.enqueue(i)

    for num in range(n-1): #마지막사람은 리턴하면서 dequeue하므로 n-1명까지만.
        for i in range(1,k):
            josephuslst.enqueue(josephuslst.dequeue()) #1부터 k-1번째 수까지 dequeue하고 바로 enqueue
        result.append(josephuslst.dequeue()) #k번째 수 dequeue
    result.append(josephuslst.dequeue())

    return result


import sys

a,b = map(int, sys.stdin.readline().split())

lst = joseph(a,b)

print('<', end="") 
print(", ".join(map(str, lst)), end="")
print(">")

