import sys
x_values=[]
y_values=[]
for i in range(3):
    x,y  = map(int, sys.stdin.readline().split())
    x_values.append(x)
    y_values.append(y)

for i in x_values:
    if x_values.count(i)==1:
        x_result = i
        
for i in y_values:
    if y_values.count(i)==1:
        y_result = i
        
        
print(x_result, y_result)