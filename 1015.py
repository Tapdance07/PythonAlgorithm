# 수열 정렬문제
import sys

# 입력 받기
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# (값, 인덱스) 쌍 만들기
target = []
for i in range(N):
    target.append((A[i], i))

# 값을 기준으로 오름차순 정렬
target.sort()

# 결과 수열 P 생성
P = [0] * N
for new_idx in range(N):
    val, original_idx = target[new_idx]
    P[original_idx] = new_idx

# 결과 출력
print(*(P))