#팰린드롬 수

#단어를 뒤에서 읽어도 똑같다면 팰린드롬이라고한다.
#수에도 적용이 가능하다. 

#무의미한 0은 앞에 올 수 없다.


import sys, copy

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    
    n_lst = list(str(n))
    sample_lst = copy.deepcopy(n_lst)

    n_lst.reverse()
    if sample_lst == n_lst:
        print('yes')
    else:
        print('no')

