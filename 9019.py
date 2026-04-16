# 4개의 D,S, L, R의 명령어를 사용하는 계산기가 있다
# 0이상 10,00 미만의 십진수를 저장한다
# 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다.
#n의 4자릿수를 d1,d2,d3,d4하고 하면
# D : n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
# S : n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L : n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R : n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
# 이 계산기를 활용하여 A를 B로 만드는 최소한의 명령어

import sys
from collections import deque

def solve():
    # 입력 받기
    line = sys.stdin.readline().rstrip().split()
    if not line: return
    A, B = map(int, line)
    
    # visited[i] = (이전_숫자, 사용한_명령어)
    # 방문하지 않은 곳은 None으로 설정
    parent = [None] * 10000
    q = deque([A])
    
    # 시작점의 부모를 자기 자신으로 설정 (루프 종료 조건)
    parent[A] = (A, "") 

    while q:
        curr = q.popleft()
        
        # 목표 도달 시 역추적 시작
        if curr == B:
            path = []
            while curr != A:
                prev_num, cmd = parent[curr]
                path.append(cmd)
                curr = prev_num
            # 역순으로 저장되었으므로 뒤집어서 출력
            print("".join(reversed(path)))
            return

        # 4가지 연산 정의
        # D: 2n mod 10000
        d_next = (curr * 2) % 10000
        if parent[d_next] is None:
            parent[d_next] = (curr, "D")
            q.append(d_next)

        # S: n-1 (0이면 9999)
        s_next = (curr - 1) % 10000
        if parent[s_next] is None:
            parent[s_next] = (curr, "S")
            q.append(s_next)

        # L: 왼편 회전
        l_next = (curr % 1000) * 10 + (curr // 1000)
        if parent[l_next] is None:
            parent[l_next] = (curr, "L")
            q.append(l_next)

        # R: 오른편 회전
        r_next = (curr % 10) * 1000 + (curr // 10)
        if parent[r_next] is None:
            parent[r_next] = (curr, "R")
            q.append(r_next)

# 테스트 케이스 실행
T_input = sys.stdin.readline().rstrip()
if T_input:
    for _ in range(int(T_input)):
        solve()