import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())


for i in range(t): #t만큼

    #n,m입력받음
    n,m = map(int, sys.stdin.readline().split())

    #중요도 리스트로 입력받음
    doc_priority = deque(list(map(int, sys.stdin.readline().split())))


    #현재 타겟의 인덱스 = m
    target_indx = deque(list(range(n)))


    #출력회수
    cnt = 0
    while doc_priority:
        if doc_priority[0] == max(doc_priority):
            cnt += 1
            doc_priority.popleft()
            if target_indx.popleft() == m:
                print(cnt)
                break


        else:
            doc_priority.append(doc_priority.popleft())
            target_indx.append(target_indx.popleft())






