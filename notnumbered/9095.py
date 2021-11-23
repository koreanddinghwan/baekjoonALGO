import sys
T = int(sys.stdin.readline().rstrip())


memo = [0,1,2,4] + [-1] * 7

def test(n):
    if memo[n] != -1:
        return memo[n]

    else:
        return test(n-1) + test(n-2) + test(n-3)
        
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(test(N))