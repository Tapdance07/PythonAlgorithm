# 최소 힙 연산
# 첫째 줄에 연산의 개수 N
# N개의 줄에는 연산에 대한 정보 나타내는 정수 x
# x가 자연수라면 배열에 x라는 값을 추가
# x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우

import heapq
import sys
N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)