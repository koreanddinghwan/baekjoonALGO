import sys
#입력받으면서 문자열 변환
a = sys.stdin.readline()
status = True
lst = []
xchecker = True
x_count = 0
for i in a: #현재 입력이 x인지 .인지부터 구분
    if i != 'X': #.이면 이전에 count된걸로 문자열 만ㄷ르어서 추가
        xchecker = False
        if x_count == 0: #0이면 이전 문자열이 .이었으므로 그냥 . 추가하고 다음 문자열 체크
            lst.append('.')
            continue
        elif x_count % 2 != 0: #0이 아니고, 2로나눈 나머지가 2가 아니면 -1출력
            status = False
            break
        elif x_count % 4 == 0: #나머지 정상수행에 대해서는해당 문자열 몫만큼 AAAA, 
            lst.append((x_count // 4) * "AAAA")
            lst.append('.')
            x_count = 0
        elif x_count % 4 == 2:
            lst.append((x_count // 4) * "AAAA" + "BB") #또는 AAAA*목 +BB
            lst.append('.')
            x_count = 0
        


    elif i == 'X':
        xchecker = True
    
    if xchecker == True:
        x_count += 1

    


if status == False:
    print(-1)
else:
    lst = lst[:-1]
    print("".join(lst))