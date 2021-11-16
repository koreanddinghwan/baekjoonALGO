import sys

count = 0
while True:
    L,P,V = map(int, sys.stdin.readline().split())
    if L == P == V == 0:
        break
    
    #연속하는 일의 묶음
    k = V // P
    #연속하는 날동안 쓸 수 있는 캠핑장일수
    a = k*L


    J = V % P
    b = min(J, L)



    count += 1
    answer = a+b

    print("Case {}: {}".format(count, answer))