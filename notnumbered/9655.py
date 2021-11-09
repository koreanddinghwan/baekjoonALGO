#나머지가 4면 게임끝남

import sys
n = int(sys.stdin.readline().rstrip())

if n % 2 == 1:
    print("SK")
else:
    print('CY')