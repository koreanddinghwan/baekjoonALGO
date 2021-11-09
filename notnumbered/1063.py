import sys

kingpos, stonepos, n = map(str,sys.stdin.readline().split())
def pos(a): #킹과 돌의 위치를 변환[X,Y]
    a_lst = list(str(a))
    alphastring = 'ABCDEFGH'
    for i in range(len(alphastring)):
        if alphastring[i] == a_lst[0]:
            x_pos = i + 1

    y_pos = int(a_lst[-1])
    return [x_pos, y_pos]

def collison(kingpos,stonepos):
    
    if kingpos == stonepos:
        return True
    else:
        return False

def outofchess(kingpos,stonepos):
    if not (kingpos[0] >= 1 and kingpos[0] <= 8 and kingpos[1] >= 1 and kingpos[1] <= 8 and stonepos[0] >= 1 and stonepos[0] <= 8 and stonepos[1] >= 1 and stonepos[1] <= 8):
        
        return True
    else:
        return False


def movement(command,kingpos,stonepos):
    if command == 'R':
        kingpos[0] = kingpos[0] + 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] + 1
            COLLISION = True

        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[0] = kingpos[0] - 1
            stonepos[0] = stonepos[0] - 1
            return kingpos, stonepos
        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] - 1

        return kingpos, stonepos

    elif command == 'L':
        kingpos[0] = kingpos[0] - 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] - 1
            COLLISION = True

        if outofchess(kingpos,stonepos) and COLLISION:
            stonepos[0] = stonepos[0] + 1
            kingpos[0] = kingpos[0] + 1
        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] + 1

            return kingpos, stonepos

        return kingpos, stonepos

    elif command == 'B':
        kingpos[1] = kingpos[1] - 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[1] = stonepos[1] - 1
            COLLISION = True

        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[1] = kingpos[1] + 1
            stonepos[1] = stonepos[1] + 1
            return kingpos, stonepos
        elif outofchess(kingpos,stonepos):
            kingpos[1] = kingpos[1] + 1

        return kingpos, stonepos


    elif command == 'T':
        kingpos[1] = kingpos[1] + 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[1] = stonepos[1] + 1
            COLLISION = True
            

        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[1] = kingpos[1] - 1
            stonepos[1] = stonepos[1] - 1
            return kingpos, stonepos
        elif outofchess(kingpos,stonepos):
            kingpos[1] = kingpos[1] - 1
        return kingpos, stonepos
    
    elif command == 'RT':
        kingpos[0] = kingpos[0] + 1
        kingpos[1] = kingpos[1] + 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] + 1
            stonepos[1] = stonepos[1] + 1
            COLLISION = True

        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[0] = kingpos[0] - 1
            kingpos[1] = kingpos[1] - 1
            stonepos[0] = stonepos[0] - 1
            stonepos[1] = stonepos[1] - 1
            return kingpos, stonepos

        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] - 1
            kingpos[1] = kingpos[1] - 1
        return kingpos, stonepos



    elif command == 'LT':
        kingpos[0] = kingpos[0] - 1
        kingpos[1] = kingpos[1] + 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] - 1
            stonepos[1] = stonepos[1] + 1
            COLLISION = True
        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[0] = kingpos[0] + 1
            kingpos[1] = kingpos[1] - 1
            stonepos[0] = stonepos[0] + 1
            stonepos[1] = stonepos[1] - 1
            return kingpos, stonepos
        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] + 1
            kingpos[1] = kingpos[1] - 1
        return kingpos, stonepos

    elif command == 'RB':
        #왕 이동
        kingpos[0] = kingpos[0] + 1
        kingpos[1] = kingpos[1] - 1
        COLLISION = False
        #왕과 돌 충돌하면 돌 이동
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] + 1
            stonepos[1] = stonepos[1] - 1
            COLLISION = True
        #돌과 왕이체스밖으로 나가면 연산취소
        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[0] = kingpos[0] - 1
            kingpos[1] = kingpos[1] + 1
            stonepos[0] = stonepos[0] - 1
            stonepos[1] = stonepos[1] + 1
            return kingpos, stonepos

        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] - 1
            kingpos[1] = kingpos[1] + 1
        return kingpos, stonepos

    elif command == 'LB':
        kingpos[0] = kingpos[0] - 1
        kingpos[1] = kingpos[1] - 1
        COLLISION = False
        if collison(kingpos,stonepos):
            stonepos[0] = stonepos[0] - 1
            stonepos[1] = stonepos[1] - 1
            COLLISION = True
            
        if outofchess(kingpos,stonepos) and COLLISION:
            kingpos[0] = kingpos[0] + 1
            kingpos[1] = kingpos[1] + 1
            stonepos[0] = stonepos[0] + 1
            stonepos[1] = stonepos[1] + 1
            return kingpos, stonepos
        elif outofchess(kingpos,stonepos):
            kingpos[0] = kingpos[0] + 1
            kingpos[1] = kingpos[1] + 1
        return kingpos, stonepos

def transtostr(kingpos,stonepos):
    alphastring = 'ABCDEFGH'
    for i in range(len(alphastring)):
        if i + 1 == kingpos[0]:
            kingpos[0] = alphastring[i]
            # print(kingpos)

        if i + 1 == stonepos[0]:
            stonepos[0] = alphastring[i]
            # print(stonepos)

    K_str = kingpos[0] + str(kingpos[1])
    S_str = stonepos[0] + str(stonepos[1])
    S = [K_str,S_str]
    return S


kingpos = pos(kingpos)
stonepos = pos(stonepos)

for i in range(int(n)):
    command  = sys.stdin.readline().rstrip()
    movement(command, kingpos,stonepos)
    # print(kingpos,stonepos)

#문자열로 변환
S = transtostr(kingpos,stonepos)
for i in S:
    print(i)


# for i in range(int(n)):
#     command  = sys.stdin.readline().rstrip()
#     for c in range(len(command)):
#         if command[c] == 'R':
#             #명령어 실행시 돌과 충돌
#             if king_x_pos + 1 == stone_x_pos and king_y_pos == stone_y_pos:
#                 #옮긴 위치가 체스판 위라면
#                 if king_x_pos + 1 <= 8 and stone_x_pos+1<=8:
#                     king_x_pos += 1
#                     stone_x_pos += 1
#                     print('KING:', king_x_pos,king_y_pos,'STONE:',stone_x_pos,stone_y_pos)

#                 else: #체스판 바깥이라면 다음 명령어로 넘어간다.
#                     break
#             else: #돌과 충돌하지는 않음
#                 # 움직인 위치가 체스판 내부라면
#                 if king_x_pos + 1 <= 8:
#                     king_x_pos += 1
#                 else: #움직인 위치가 체스판 외부면 바깥for문으로넘어가 다음명령어실행
#                     break

#         elif command[c] == 'L':
#             #명령어 실행시 돌과 충돌
#             if king_x_pos - 1 == stone_x_pos and king_y_pos == stone_y_pos:
#                 #옮긴 위치가 체스판 위라면
#                 if king_x_pos - 1 >= 1 and stone_x_pos-1>=1:
#                     king_x_pos -= 1
#                     stone_x_pos -= 1
#                     print('KING:', king_x_pos,king_y_pos,'STONE:',stone_x_pos,stone_y_pos)

#                 else: #체스판 바깥이라면 다음 명령어로 넘어간다.
#                     break
#             else: #돌과 충돌하지는 않음
#                 # 움직인 위치가 체스판 내부라면
#                 if king_x_pos - 1 >= 0:
#                     king_x_pos -= 1
#                 else: #움직인 위치가 체스판 외부면 바깥for문으로넘어가 다음명령어실행
#                     break
        
#         elif command[c] == 'B':
#             if king_y_pos - 1 == stone_y_pos and king_x_pos == stone_x_pos:
#                 #옮긴 위치가 체스판 위라면
#                 if king_y_pos - 1 >= 1 and stone_y_pos-1>=1:
#                     king_y_pos -= 1
#                     stone_y_pos -= 1
#                     print('KING:', king_x_pos,king_y_pos,'STONE:',stone_x_pos,stone_y_pos)

#                 else: #체스판 바깥이라면 다음 명령어로 넘어간다.
#                     break
#             else: #돌과 충돌하지는 않음
#                 # 움직인 위치가 체스판 내부라면
#                 if king_y_pos - 1 >= 0:
#                     king_y_pos -= 1
#                 else: #움직인 위치가 체스판 외부면 바깥for문으로넘어가 다음명령어실행
#                     break
            
#         elif command[c] == 'T':
#             if king_y_pos + 1 == stone_y_pos and king_x_pos == stone_x_pos:
#                 #옮긴 위치가 체스판 위라면
#                 if king_y_pos + 1 <= 8 and stone_y_pos+1 <= 8:
#                     king_y_pos += 1
#                     stone_y_pos += 1
#                     print('KING:', king_x_pos,king_y_pos,'STONE:',stone_x_pos,stone_y_pos)

#                 else: #체스판 바깥이라면 다음 명령어로 넘어간다.
#                     break
#             else: #돌과 충돌하지는 않음
#                 # 움직인 위치가 체스판 내부라면
#                 if king_y_pos + 1 <= 8:
#                     king_y_pos += 1
#                 else: #움직인 위치가 체스판 외부면 바깥for문으로넘어가 다음명령어실행
#                     break

        
# #각 명령어의 결과로 킹이나 돌의 위치가 같다면 돌을 킹과 같은 방향으로 한칸이동
# #단 킹이나 돌이 체스판 밖으로 나가면 명령어 패스

# #킹이 움직일때 돌과 위치가 같아짐->같이 같은 방향으로 한칸씩 단, 
# # 돌이 체스판 바깥으로 나가면 명령어실행취소

# #킹이 체스판 바깥으로 나가면 명령어 생략
# print(king_x_pos,king_y_pos)