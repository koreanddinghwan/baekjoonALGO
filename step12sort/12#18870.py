import sys

n = int(sys.stdin.readline().rstrip())
m = list(map(int, sys.stdin.readline().split()))

#m에 있는 원소들 집합으로 중복제거
m_set = set(m)

#다시 리스트로 만들어 정렬
m_set_lst = list(m_set)
sorted_m_set_lst = sorted(m_set_lst)

d = {}
for i in range(len(sorted_m_set_lst)):
    d.setdefault(sorted_m_set_lst[i],i)

answer = []
for i in m:
    answer.append(str(d[i]))
print(" ".join(answer))



#자기자신보다 작은수의 개수가 자신의 좌표값







