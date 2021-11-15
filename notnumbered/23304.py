import sys,math

n = sys.stdin.readline().strip()


    
def pelin(s):
    result = True   
    half = math.floor(len(s)/2)

    for i in range(half):
        if s[i] != s[len(s) - i -1]:
            return False

    half_string = s[:half]
    half = math.floor(len(half_string) / 2)

    for i in range(half):
        if half_string[i] != half_string[len(half_string) - i -1]:
            return False

    return True





if pelin(n) == True:
    print('AKARAKA')
else:
    print('IPSELENTI')

