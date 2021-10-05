import sys

def d(n):
    num_list = list(map(int,str(n)))
    next_num= n + sum(num_list)
    return next_num

lst = []
for num in range(1,10000):
    lst.append(d(num))
    
print(lst)    

full_list = list(range(1,10000))
# for i in full_list:
    # if i not in lst:
    #     print(i)
