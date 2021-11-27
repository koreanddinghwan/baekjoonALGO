import heapq,sys

n = int(sys.stdin.readline().rstrip())
heap = []
heapitemcount = 0

#heapq는 튜플이 주어지면 첫 원소를 기준으로 heap을 구성한다
#따라서 첫 원소에 원래 값의 -값을 붙여주면 좌표상 좌우대칭이되며 최대힙이 구성된다.

for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    if data == 0:
        if heapitemcount == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
            heapitemcount -= 1
    else:
        heapq.heappush(heap, (-data, data))
        heapitemcount += 1


