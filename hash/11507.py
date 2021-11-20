import sys


input = sys.stdin.readline().rstrip()

ptable = {}
ktable = {}
htable = {}
ttable = {}
status = True
for i in range(len(input)):
    if input[i].isalpha():
        #다음 2개 문자열 만들기
        a = input[i+1] + input[i+2]

        if input[i] == "P":
            try:
                ptable[a]
                status = False
                break
            except:
                ptable.setdefault(a,0)

        elif input[i] == "K":
            try:
                ktable[a]
                status = False
                break
            except:
                ktable.setdefault(a,0)
        elif input[i] == "H":
            try:
                htable[a]
                status = False
                break
            except:
                htable.setdefault(a,0)
        elif input[i] == "T":
            try:
                ttable[a]
                status = False
                break
            except:
                ttable.setdefault(a,0)

if status == False:
    print('GRESKA')
else:
    print(13- len(ptable),13- len(ktable),13- len(htable),13- len(ttable))