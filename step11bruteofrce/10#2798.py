import sys
n,m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

lst = [0]
n = len(card)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if card[i]+card[j]+card[k] <= m and card[i]+card[j]+card[k] > sum(lst):
                lst = []
                lst.append(card[i]+card[j]+card[k])

    

print(sum(lst))