import sys

N,M = map(int, sys.stdin.readline().split())
#이름:그룹이름으로 저장하는 딕셔너리
name_group_dict = {}
#그룹이름:[멤버이름] 으로 저장하는 딕셔너리
group_name_dict = {}

#입력받는 곳, N만큼 그룹 입력받아야함
for group in range(N):
    #그룹의 이름과 멤버수를 입력받음
    group_name = sys.stdin.readline().rstrip()
    member_num = int(sys.stdin.readline().rstrip())


    member_lst = []
    #딕셔너리로 이름:그룹이름으로 키값을 이름으로하는 딕셔너리에 추가
    for member_number in range(member_num):
        member_name = sys.stdin.readline().rstrip()
        name_group_dict.setdefault(member_name,group_name)
        member_lst.append(member_name)

    member_lst.sort()
    group_name_dict.setdefault(group_name,member_lst)
    




for _ in range(M):
    questionname = sys.stdin.readline().rstrip()
    kindofquestiond = int(sys.stdin.readline().rstrip())
    if kindofquestiond == 1:
        print(name_group_dict[questionname])
    else:
        for i in group_name_dict[questionname]:
            print(i)