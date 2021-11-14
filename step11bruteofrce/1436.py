'''
666 1번째
1666 2번재
2666 3번째
3666 4번째
4666 5번째
5666 6번째!!
6660 7번째!!
6661 8번째
6662 9번째'''



import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range(2700000):
    if '666' in str(i):
        cnt +=1

    if cnt == n:
        print(i)
        break

else:
    print('no')
