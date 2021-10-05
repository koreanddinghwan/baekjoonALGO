# 문제
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 
# 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.

# 싸이클 연산

# 26의 다음 숫자는 68이다.
# 68의 다음 숫자는 84이다.
# 

# 0보다크거나같고, 99보다작거나같기에 10으로 나누면 밑의 공식이 성립한다.
# 입력값의 몫->// 나머지->%

# 인덱스로 접근할 것인가, int로 접근할 것인가에 따라 문제풀이가 달라진다.
# +로인해 더하는 연산이 어차피 필요하기에 정수접근으로가자.

# 주어진 값
n = int(input())

# 원래 주어진 값을 한 변수에 저장한다.
original = n

# 싸이클 계산변수
cycle = 0

a = True
while a:
    # 더한값의 계산, 다음 숫자는 주어진 숫자 n을 % 10으로 나눈 값을 십의자리로하고 26%10 = 6, 6*10
    # 각 자리수의 합을 10으로 나눈수의 나머지가 된다. (26//10+26%10)%10 8
    n = 10*(n % 10) + ((n % 10 +  n // 10) % 10)
    
    #싸이클 계산
    cycle += 1
    
    #한번 연산이 끝나고 탈출조건 체크
    if n == original:
        break
    
print(cycle)


# 출력
# 첫째 줄에 N의 사이클 길이를 출력한다.