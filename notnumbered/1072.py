import sys


# x,y = map(int, sys.stdin.readline().split())
# origin_z = int(y / x * 100)
# print(origin_z)


print([False] * 100000000)
"""

10억을 더했음에도 바뀌지 않는다 => -1

1회차 => 5억과  10억을 각각 더한다, 
1. 5억과 10억을 더했는데, 둘다 바뀌면, 서치대상은 5억을 넣었을때이다
2. 5억에서만 바뀌면 서치대상은 역시 5억이다.
3. 10억에서만 바뀌면 서치대상은 (10억-5억)/2


"""






