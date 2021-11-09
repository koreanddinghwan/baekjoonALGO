import sys

score_lst = []
for i in range(10):
    score_lst.append(int(sys.stdin.readline().rstrip()))

ac_data = []
for i in range(len(score_lst)):
    data = sum(score_lst[0:i+1])
    ac_data.append(data)


under = []
upper = []
is_100 = False

for i in ac_data:
    if i == 100:
        is_100 = True
        
    elif i > 100:
        upper.append(i)
    elif i < 100:
        under.append(i)

isupper = True
if upper == []:
    isupper = False
else:
    minupper = min(upper)

isunder = True
if under == []:
    isunder = False
else:
    maxunder = max(under)

if is_100 == True:
    print('100')
elif isupper == False:
    print(maxunder)
elif isunder == False:
    print(minupper)

else:
    if abs(100-minupper) > abs(100-maxunder):
        print(maxunder)
    elif abs(100-minupper) < abs(100-maxunder):
        print(minupper)
    elif abs(100-minupper) == abs(100-maxunder):
        print(minupper)