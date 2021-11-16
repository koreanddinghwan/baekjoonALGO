import sys
n=8
scoredict = {}
scorelst = []
for i in range(n):
    score = int(sys.stdin.readline().rstrip())
    scorelst.append(score)
    scoredict.setdefault(score,i)


scorelst.sort()
scorelst.reverse()



print(sum(scorelst[:5]))
dicnum = []
for i in range(5):
    dicnum.append(str(scoredict[scorelst[i]]+1))
dicnum.sort()
print(" ".join(dicnum))