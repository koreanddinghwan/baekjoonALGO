# class queue():
#     def __init__(self): #객체 생성함수
#         self.items = []
#         self.front_value = 0 #큐가 현재 인식하는 front값
    

#     def push(self, value): #큐 추가
#         self.items.append(value)

#     def pop(self): 
#         if len(self.items) == self.front_value: #현재 인식하고있는 첫 인덱스frontvalue가 큐길이와 동일
#             return -1

#         else:
#             x = self.items[self.front_value] #첫 인덱스 저장
#             self.front_value += 1 #인식하는 front index 1 증가
#             return x

#     def size(self):
#         return len(self.items[self.front_value:])

#     def empty(self):
#         if len(self.items) == self.front_value: #동일
#             return 1
#         else:
#             return 0

#     def front(self):
#         if len(self.items) == self.front_value: #동일
#             return -1

#         else:
#             x = self.items[self.front_value]
#             return x
        

#     def back(self):
#         if len(self.items) == self.front_value:
#             return -1
#         else:
#             return self.items[-1]


# import sys
# n = int(sys.stdin.readline().rstrip())

# Q = queue()

# for i in range(n):
#     usr_inp = list(sys.stdin.readline().split())
#     if usr_inp[0] == 'push':
#         Q.push(int(usr_inp[-1]))

#     if usr_inp[0] == 'front':
#         print(Q.front())

#     if usr_inp[0] == 'pop':
#         print(Q.pop())

#     if usr_inp[0] == 'size':
#         print(Q.size())

#     if usr_inp[0] == 'empty':
#         print(Q.empty())

#     if usr_inp[0] == 'back':
#         print(Q.back())

#############################################################
#일반적인 선형배열로 만들 경우,시간초과된다.
#연산당 시간복잡도가 O(1)이려먼
#len(self.items[self.front_value:]) 여기서 시간복잡도가 늘어난다.
#만약 현재 리스트에 아이템이 2000000개가 있으면  self.front_value가 1일때 1999999개를 읽어와야하는 
#대참사!가 벌어진다.!!!!
#리스트 슬라이싱의 시간복잡도의 경우 O(n+k)이다

from collections import deque
import sys

q = deque()


n = int(sys.stdin.readline().rstrip())


for i in range(n):
    usr_inp = list(sys.stdin.readline().split())
    if usr_inp[0] == 'push':
        q.append(usr_inp[-1])
        

    if usr_inp[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    if usr_inp[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    

    if usr_inp[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    if usr_inp[0] == 'size':
        print(len(q))

    if usr_inp[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    

