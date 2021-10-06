# 문제 정의
# 수를 9개 각각 입력받고, 최댓값과 최댓값의 인덱스를 출력한다.





#풀이
# 각각 입력받는 수를 리스트에 저장한 다음,  리스트의 최댓값과 리스트에서 최댓값의 인덱스+1을 출력하면된다.
# 인덱스와 우리가 일반적으로 생각하는 순서는 1의 차이가 있으므로 +1을 해줘야한다.
import sys

n_lst = []
for i in range(9):
    n = int(sys.stdin.readline().rstrip())
    n_lst.append(n)

print(max(n_lst))
print(n_lst.index(max(n_lst))+1)


