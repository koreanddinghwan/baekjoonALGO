## 오 이런 싸발!

import sys
from collections import Counter, deque

test = int(sys.stdin.readline().rstrip())


for _ in range(test):

    #명령문 입력
    command = sys.stdin.readline().rstrip()

    #명령문 속 문자열 개수
    count = Counter(command)
    Rcount = count['R']
    Dcount = count['D']



    #데이터 개수 입력
    n = int(sys.stdin.readline().rstrip())
    data = sys.stdin.readline().rstrip()
    Q = deque()
    if n == 0:
        datalst = []

    else:
        #데이터입력
        data = data.replace('[', '')
        data = data.replace(']', '')
        datalst = list(map(int, data.split(',')))
        for i in datalst:
            Q.append(i)

    if Dcount > n:
            print('error')
            continue



    #명령어 실행
    Onpopleft = True

    for c in command:

        if c =='R':
            if Onpopleft == True:
                Onpopleft = False
            else:
                Onpopleft = True


        else:
            if c == 'D':
                if len(Q) == 0:
                    print('error')
                    break
                if Onpopleft:
                    Q.popleft()

                else:
                    Q.pop()

    if Rcount % 2 == 0:
        print("[{}]".format(",".join(list(map(str,Q)))))

    else:
        Q.reverse()
        print("[{}]".format(",".join(list(map(str,Q)))))








