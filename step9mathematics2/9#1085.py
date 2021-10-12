import sys

x,y,w,h = map(int,sys.stdin.readline().split())

lst = [x,y,h-y,w-x]

print(min(lst))