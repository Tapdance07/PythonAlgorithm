# 절댓값 힙에 대한것이다
# 배열에 정수 X 를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
# 절댓값이 가장 작은 값이 여러 개일때는, 가장 작은 수를 출력하고 그 값을 배열에서 제거한다.
# 정렬은 절댓값으로 힙 정렬을 하고 출력할때는 원상태로 출력해라



import sys
import heapq

N = int(sys.stdin.readline().rstrip())

heap = []


for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
