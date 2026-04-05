# 이중 우선순위 큐는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할수 있는 자료구조
# 유선 순위에 따라서 명령을 시행한다.
# 하나는 데이터를 삽입하는 것이고 하는 삭제하는 연산인데
# 삭제하는 것도 2가지로 나뉘는데 하나는 우선순이가 가장 높은 것을 삭제하고, 하나는 우선순위가 가장 낮은 것을 삭제한다.
# Q에 들어간 각 정수의 값 자체가 우선순위이다.
# 최종적으로 q에 저장된 데이터 중 최댓값과 최솟값을 출력한다.

import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙
    k = int(sys.stdin.readline().rstrip())
    visited = [False] * k
    
    for i in range(k):
        cmd = sys.stdin.readline().rstrip().split()
        command = cmd[0]
        n = int(cmd[1])
        # st 가 I이면 삽입연산
        # st 가 D 1이면 최댓값 삭제,  n이 -1이면 최솟값을 갓제한다.
        if command == 'I':
            heapq.heappush(min_h,(n,i))
            heapq.heappush(max_h,(-n,i))
            visited[i] = True
        elif n == 1:
            # 여기가 최댓값 삭제
            while max_h and not visited[max_h[0][1]]:
                heapq.heappop(max_h)
            if max_h:
                visited[max_h[0][1]] = False
                heapq.heappop(max_h)
        else:
            while min_h and not visited[min_h[0][1]]:
                heapq.heappop(min_h)
            if min_h:
                visited[min_h[0][1]] = False
                heapq.heappop(min_h)
                
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    if not min_h or not max_h:
        print("EMPTY")
    else:
            # 최대 힙은 음수로 저장했으므로 다시 마이너스를 붙여 출력
        print(f"{-max_h[0][0]} {min_h[0][0]}")