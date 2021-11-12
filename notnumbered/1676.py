import sys

n = int(sys.stdin.readline().rstrip())
count = 0
count += n // 5 

count += n // 25
count += n // 125
print(count)