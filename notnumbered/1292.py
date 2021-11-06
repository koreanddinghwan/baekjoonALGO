lst = []

for i in range(1,49):
    num = i
    for n in range(i):
        lst.append(num)


from sys import stdin as s

a,b = map(int, s.readline().split())
print(sum(lst[a-1:b]))
