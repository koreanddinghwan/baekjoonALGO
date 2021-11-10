import sys
n = int(sys.stdin.readline().rstrip())

if n == 0:
    n = -1
res = 2432902008176640000
for i in range(20,0,-1):
    res = res/i
    if n >= res:
        n = n - res
    
    
if n == 0.0:
    print('YES')
else:
    print('NO')

# import sys,math,itertools

# n = int(sys.stdin.readline().rstrip())
# lst = []
# for i in range(0,21):
#     lst.append(math.factorial(i))
# for i in range(0,21):
#     a = list(itertools.permutations(lst,i))
#     for i in range(len(a)):
#         if sum(a[i]) == n:
#             print('YES')
#             break

# else:
#     print('NO')

'''
팩토리얼의 특징으로,
n팩토리얼이 있을때, 이 팩토리얼보다 큰 수를 찾기 위해서는 
n팩토리얼은 반드시 포함하고,
이보다 작은 수들 을 조합해 찾아내어야한다는 것이다. 
가령 30이 팩토리얼 조합으로 나타내지는지 찾기위해서는
30 - k! > 0 인 k가 4!(24)이므로
4!과 이보다 작은 다른 팩토리얼들의 조합으로 찾아내야한다. 


이제 찾아야하는것은 30(입력값) - 4! = 6을 만드는 조합인데,
6또한 3!만으로, 혹은 3!과 다른 팩토리얼 간 조합으로 찾아내야한다는 것이다. 
최대숫자로 20팩토리얼이 주어지므로,  
20팩토리얼을 20부터 1까지 차례로 나누어 
n보다 처음으로 작아지는 숫자가 현재 입력값보다 작으면서, 가장 큰 팩토리얼이 될 것이다.  
이때, 이 팩토리얼을 입력값으로부터 빼고,
나머지 입력값에 대해서 다음 숫자로 검증을 반복하게된다.  

검증을 완료하고, 남은 숫자가 0이라면 팩토리얼 조합으로 만들 수 있다는 것이며,
숫자가 남는다면 만들 수 없는 숫자라는 의미이다.
'''