import sys,math
n = int(sys.stdin.readline().rstrip())

heightweight_lst = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    heightweight_lst.append([x,y])

gradelst = []
for person in heightweight_lst:
    a = [check for check in heightweight_lst if check != person]
    grade = 1
    for i in a:
        if person[0] < i[0] and person[1] < i[1]:
            grade += 1
    gradelst.append(str(grade))

print(" ".join(gradelst))