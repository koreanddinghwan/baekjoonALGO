import sys
n = sys.stdin.readline().rstrip()

cycle = 0

def d(n):
    global cycle
    a = list(map(int,str(n)))
    if a[0] - a[1] == a[1] - a[-1]:
        cycle += 1
            
            
for i in range(1,int(n)+1):
    if i < 100:
        cycle += 1
    else:
        d(i)
    
print(cycle)
