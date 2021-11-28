import sys
import heapq

n = int(sys.stdin.readline().rstrip())

#왼쪽힙과 오른쪽힙을 나누어서 저장한다. 

#저장하는 기준은 자료수가 같다면 왼쪽에, 그렇지 않으면 오른쪽 힙이다.
#저장 후, 데이터를 검증해야하는데, 왼쪽힙의 최대값과 오른쪽힙의 최소값 중, 
#오른쪽 힙의 최소값이 더 작다면, 둘의 위치를 바꿔주자
#그리고 왼쪽힙에서 최대값을 출력한다.


left = []
right = []

for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    ## 데이터 입력파트
    if len(left) == len(right):
        #최대힙이므로 -붙여서
        heapq.heappush(left, (-data, data))
    else:
        heapq.heappush(right,data)

    ## 데이터 검증
    ##왼쪽 힙의 최대값과 오른쪽힙의 최소값중 오른쪽힙이 더 작으면 위치바꾸기

    if len(left) != 0 and len(right) != 0:
        if left[0][1] > right[0]:
            L = heapq.heappop(left)[1]
            R = heapq.heappop(right)
            heapq.heappush(left, (-R, R))
            heapq.heappush(right, L)

            


    
    ##출력파트
    #왼쪽힙 인덱스[0][1]데이터 출력
    print(left[0][1])
    