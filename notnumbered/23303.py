import sys
n= sys.stdin.readline().rstrip()

d_index = []
for i in range(len(n)):
    if n[i] == 'd' or n[i] == 'D':
        d_index.append(i)



status=False
for i in d_index:
    if i != (len(n)-1):
        if n[i+1] == '2':
            status=True

if status == True:
    print('D2')
else:
    print('unrated')

