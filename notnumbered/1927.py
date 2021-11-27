import heapq, sys
n = int(sys.stdin.readline().rstrip())
heap = []
h_itemcount = 0
for i in range(n):
    data = int(sys.stdin.readline().rstrip())
    if data == 0:
        if h_itemcount == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
            h_itemcount -= 1
    else:
        heapq.heappush(heap, data)
        h_itemcount += 1