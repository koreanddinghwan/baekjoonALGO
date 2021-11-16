# 다솜이는 은진이의 옆집에 새로 이사왔다. 
# 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 
# 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. 
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)



import sys
from collections import Counter
import math

n = sys.stdin.readline().rstrip()


#문자열로 입력된 각 숫자의 개수를 세기
m = Counter(n)


#6과 9는 1세트당 두개 합쳐서 2개 나올 수 있음. 
#6과 9의 개수를 합한것 /2 의 반올림 만큼이 필요하며,(6699라면 2세트, 99999는 3세트)
#이 수와 각 자리수의 개수 중 가장 큰 것이 총 필요한 세트의 개수

six_nine = math.ceil((m["6"] + m["9"])/2)

a = [i for i in range(10) if i != 6 and i != 9]
lst_except_six_nine = []
for i in a:
    lst_except_six_nine.append(m[str(i)])


#합쳐서 최고숫자 찾기

lst_except_six_nine.append(six_nine)
print(max(lst_except_six_nine))





