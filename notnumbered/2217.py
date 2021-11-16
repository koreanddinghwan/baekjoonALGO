import sys

t = int(sys.stdin.readline().rstrip())


#3개 로프인경우
# 10 15 20 -> 3개다-> 30중량, 10제외->30, 
# 5 10 15 -> 3개다-> 15중량, 5제외->20
# 5 10 15 20 25 30->
# 최대 30
# 5제외해면 최대 50
##가장 작은 수들을 제외해가면서 개선되면 그 숫자를 제외한다.  



ropelst = []
for i in range(t):
    rope = int(sys.stdin.readline().rstrip())
    ropelst.append(rope)

length = len(ropelst)
ropelst.sort()
firsttotal = length * ropelst[0]
# print(ropelst)

for i in range(1,length):
    if (length - i) * ropelst[i] >= firsttotal:
        firsttotal = (length - i) * ropelst[i]
    

print(firsttotal)