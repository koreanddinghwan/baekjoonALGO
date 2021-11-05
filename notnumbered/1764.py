import sys

n,m = map(int, sys.stdin.readline().split())

never_heard_people=[]
never_seen_people=[]


for a in range(n):
    never_heard = sys.stdin.readline().rstrip()
    never_heard_people.append(never_heard)

for b in range(m):
    never_seen = sys.stdin.readline().rstrip()
    never_seen_people.append(never_seen)
s1 = set(never_heard_people)
s2 = set(never_seen_people)

inter = s1.intersection(s2)
inter = list(inter)


print(len(inter))
inter.sort()
for i in inter:
    print(i)