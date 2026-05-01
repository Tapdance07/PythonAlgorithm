import sys
from collections import deque

def solve():

    line = sys.stdin.readline().rstrip()
    if not line:
        return
    n, m = map(int, line.split())
    
    board = list(range(101))
    
    for _ in range(n + m):
        u, v = map(int, sys.stdin.readline().split())
        board[u] = v

    visited = [-1] * 101
    
    queue = deque([1])
    visited[1] = 0

    while queue:
        curr = queue.popleft()
        
        if curr == 100:
            print(visited[curr])
            return


        for i in range(1, 7):
            next_pos = curr + i
            
            if next_pos <= 100:
                final_pos = board[next_pos]
                
                if visited[final_pos] == -1:
                    visited[final_pos] = visited[curr] + 1
                    queue.append(final_pos)


solve()