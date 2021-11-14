'''
MN크기의 보드를 잘라 88체스판으로 만들기
체스판을 잘라서 몇개의 정사각형을 다시 칠했을 때,
최소로 칠해야하는 정사각형의 개수
'''

import sys

n,m = map(int, sys.stdin.readline().split())

#왼쪽 상단이 흰색인 경우
wb = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

#왼쪽 상단이 검은색인 경우
bw = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]



chess = []
#체스판을 문자열형태로 저장
for i in range(n):
    row = sys.stdin.readline().rstrip()
    chess.append(row)

'''
8*8로 잘라내는 경우의 수는 n=10,m=13일때
왼쪽 끝 상단을 기준으로
chess의 [0][] ~ [10-8][]를 각각
[][0]~ [][13-8]까지 반복한 것임.
'''

#왼쪽상단좌표구하기
lefttop = []
for row in range(0,n-8+1):
    for column in range(0,m-8+1):
        #왼쪽상단좌표
        lefttop.append([row,column])

#왼족 상단 좌표들에 대해서 각각 리스트를 구하기
lefttop_chesslst = []
for i in lefttop:
    #i에는 좌표값이 들어가있음.
    #i[0] = 0, i[1] = 0이므로
    # chess[i[0]][i[1]:i[1]+8]을
    # chess[i[0]+8][i[1]:i[1]+8]까지반복
    lst= []
    for r in range(0,8):
        lst.append(chess[i[0]+r][i[1]:i[1]+8])
    lefttop_chesslst.append(lst)

mincntlst = []
for i in lefttop_chesslst:
    cnt = 0
    for row in range(8):
        for c in range(8):
            if i[row][c] != bw[row][c]:
                cnt += 1
    mincntlst.append(cnt)

    cnt = 0
    for row in range(8):
        for c in range(8):
            if i[row][c] != wb[row][c]:
                cnt += 1

    mincntlst.append(cnt)

print(min(mincntlst))