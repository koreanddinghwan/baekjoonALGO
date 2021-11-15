import sys

t = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().split()))


def uclid(a,b):
    r = a%b
    if r == 0:
        return b

    return uclid(b,r)

for i in range(1,len(lst)):
    #lst[0]과 lst[i]의 최대공약수 찾기
    if lst[0] > lst[i]:
        bignum = lst[0]
        smallnum = lst[i]
        num = uclid(bignum,smallnum)
        print("{}/{}".format(lst[0]//num,lst[i]//num))
    elif lst[0] < lst[i]:
        bignum = lst[i]
        smallnum = lst[0]
        num = uclid(bignum,smallnum)
        print("{}/{}".format(lst[0]//num,lst[i]//num))

    else:
        num == lst[0]
        print("{}/{}".format(1,1))


    