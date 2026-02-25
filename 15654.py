# N,M 을 주는데 길이가 M인 수열을 모두 구하기
# 즉 N개의 자연수 중에서 M개를 고른 수열이다

N,M = map(int, input().split())
A = list(map(int, input().split()))

A.sort() # 오름차순 정렬

# 숫자의 사용 여부를 확인하는 배열
visited = [False] * N

def backtracking(path):
    # 목표 길이 M에 도달하면 출력
    if len(path) == M:
        print(*path)
        return

    # 매번 0부터 N까지 모든 숫자를 후보로 검토
    for i in range(N):
        if not visited[i]: # 아직 사용하지 않은 숫자라면
            visited[i] = True # 사용 표시
            path.append(A[i])
            
            backtracking(path) # 다음 숫자 고르러 가기
            
            path.pop() # 되돌아오기 (백트래킹)
            visited[i] = False # 사용 표시 해제

backtracking([])