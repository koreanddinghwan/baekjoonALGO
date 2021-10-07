# import sys
# a,b,v = map(int, sys.stdin.readline().split())


# h = 0
# d = 0
# while h < v:
#     h = h + a
#     d = d + 1
#     if h >= v:
#         break;
#     h = h - b
    
# print(d)
# 위코드는 시간초과


# 다 올라가기 전날 밤은 수식으로 바로 계산이 가능하다.
# v-a를 해주면 다 올라가기 전날까지 올라가야할 높이가되고, 이를 하루에 올라가는 높이로 나누면 다 올라가는 전날까지의 날짜가된다.
# 여기서 주의해야할 점은 조금 올라가도 하루를 쓰는 것이기에 소수점이 나온다면 이것도 +1이라고 ㅎ야하는 것이다.
# 따라서 +1을 해주면 다음날 달성하는 높이가된다.
import sys, math
a,b,v = map(int, sys.stdin.readline().split())

print(math.ceil((v-a)/(a-b))+1)

