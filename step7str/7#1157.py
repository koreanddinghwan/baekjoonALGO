# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


import sys
n = sys.stdin.readline().rstrip().upper()

a = list(map(chr, range(65,91)))
alphacountlst = []
for i in a:
    count_ = n.count(i)
    alphacountlst.append(count_)

# 만약 alphalst의 최댓값이 다른 alpahlst의 최댓값과 같은경우, ?출력하고 for문 종료

if alphacountlst.count(max(alphacountlst)) > 1:
    print("?")
else:
        # 최댓값이 있는 alphalst의 인덱스 값을 a의 인덱스값에 넣기
    print(a[alphacountlst.index(max(alphacountlst))])
        

