# import sys

# from collections import Counter

# n = int(sys.stdin.readline().rstrip())

# lst = list(map(int, sys.stdin.readline().split()))

# #정답을 저장하기위한 리스트
# ngf = [-1 for _ in range(n)]

# #스택,
# stack = [0]

# count = dict(Counter(lst))

# for i in range(1,n):
#     #스택에 값이 들어있고, 스택의 마지막값의 카운트가 현재 값의 카운트보다작다면
#     while stack and count[lst[stack[-1]]] < count[lst[i]]:
#         #스택을 풀고 오등큰수를 부여
#         ngf[stack.pop()] = lst[i]

#     #while문에서 빠져나왔다는건, 스택에 더이상 오등큰수를 부여할 수가 없다는것.
#     #다음 i가 검증하도록 stack에 i부여
#     stack.append(i)

# print(" ".join(map(str, ngf)))

import sys
from collections import Counter
import heapq

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))

#정답을 저장하기위한 리스트
ngf = [-1 for _ in range(n)]


heap = []

count = dict(Counter(lst))
for i in range(n-1,-1,-1):
    while heap and heap[0][0] <= count[lst[i]]:
        heapq.heappop(heap)

    if len(heap) == 0:
        ngf[i] = -1

    else:
        ngf[i] = heap[0][1]

    heapq.heappush(heap,(count[lst[i]],lst[i]))

print(" ".join(map(str,ngf)))