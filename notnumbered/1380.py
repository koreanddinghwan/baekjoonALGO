import sys


class stack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        if value in self.lst:
            self.lst.remove(value)
        else:
            self.lst.append(value)

    def __str__(self):
        return str(self.lst[0])


count = 1

while True:
    num_st = int(sys.stdin.readline().rstrip()) #학생 수
    if num_st == 0:
        break
    st_lst = []
    for i in range(num_st): #학생 수만큼 학생이름 입력받아 리스트에 저장
        st_name = sys.stdin.readline().rstrip()
        st_lst.append(st_name)

    #채킹할스택 정의
    s = stack()

    ##인원수*2 -1 만큼출력
    for i in range(len(st_lst)*2 - 1):
        v, p = map(str, sys.stdin.readline().split())
        s.push(v)

    print(count, st_lst[int(s.lst[0]) - 1])

    count += 1











