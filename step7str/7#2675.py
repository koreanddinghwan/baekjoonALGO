# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 
# 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
import sys
t = int(sys.stdin.readline().rstrip())
# 출력
# 각 테스트 케이스에 대해 P를 출력한다.


# 주어진 t에 대해서 t만큼 테스트 개수를 입력받는다.
for case in range(t):
    r, s = map(str, sys.stdin.readline().split())
    # 입력받은 s의 각 문자에 대해서
    for i in range(len(s)):
        # int(r)*s[i]로 각 문자열을 r만큼 곱해주고, 줄바꿈문자는 삭제.
        print(int(r)*s[i], end="")
    # 한 case가 끝나면 줄바꿈 문자를 출력하고 다음 케이스를 입력받는다.
    print(end="\n")