import sys


#각 이름이 추가될때 해시테이블의 개수도 1씩 증가해야한다.  
#전체 값을 유지
total = 0
trees = {}
lst = set()

while True:
    n = sys.stdin.readline().rstrip()
    if n == '':
        break

    lst.add(n)

    try:
        trees[n] = trees[n] + 1
        total += 1
    except:
        trees[n] = 1
        total += 1


sortedlst = sorted(lst)

for i in sortedlst:
    print(i, "{:.4f}".format(int(trees[i])/total*100))

