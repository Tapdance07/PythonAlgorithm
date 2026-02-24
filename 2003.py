# N개의 수로 된 수열 A[1], A[2], ..., A[N]이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
# 입력 N M
# 수열 A[1], A[2], ..., A[N]
# 출력 M이 되는 경우의 수


N,M = map(int, input().split())
A = list(map(int, input().split()))

# 브루트포스 알고리즘 적용
# 인덱스 1번부터 M이되는 값까지 계산해서 몇개인지 확인하기
# M을 초과하는 순간 인덱스 건너뛰기

# count = 0
# for i in range(N):
#     sum = 0
#     for j in range(i,N):
#         sum += A[j]
#         if sum == M:
#             count +=1
#             break
#         elif sum > M:
#             break
# print(count)

# 이게 가장 기본적인 브루트포스 알고리즘이다.
# 하지만 시간초과가 발생하는 것으로 보며 누적합을 사용한다.

count = 0
sum = 0
end = 0
for start in range(N):
    # sum이 M보다 작으면 end를 계속 이동하며 더함
    while sum < M and end < N:
        sum += A[end]
        end += 1
    
    # 합이 M과 같으면 카운트 증가
    if sum == M:
        count += 1
    
    # 다음 start로 넘어가기 전에 현재 start 원소를 합에서 제외
    sum -= A[start]

print(count)