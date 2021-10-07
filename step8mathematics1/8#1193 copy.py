n = int(input())

# 인풋으로 받은 수 |5가정|5|4
m = n

# 현재 항의 개수 |0|1|
s = 0

#범위내의 0부터 1억까지 |0|1|2|
for i in range(10000000000):
    
    # | 0 + 0|0+1|1+2|
    s += i
    # |0 > 5->x|x|x|
    if s >= n:
        if i % 2 == 0:
            print("%d/%d"%(m,i+1-m))
        else:
            print("%d/%d"%(i+1-m,m))
        break
    # |5 - 0|5-1=4|
    m -= i