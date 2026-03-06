# 이분탐색
# 나무 M미터 필요하다.
# 절단기에 높이 H를 지정하면 나무가 H보다 큰 나무는 H만큼 잘리고, H보다 작은 나무는 잘리지 않는다.
# 절단기에 설정할 수 있는 높이의 최댓값을 구하시오.
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees) # 정렬 대신 max() 사용
# 결국엔 계속 값의 절반씩만 사용하는 것이기때문에 맥스와 제일 작은 0만 맨처음에 지정을 해준다면
# 스스로 정렬된 것처럼 행동하게 된다.
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    
    
    # 잘린 나무 길이 합산
    total = sum(tree - mid for tree in trees if tree > mid)
    # 이분 탐색 로직
    if total >= M:      # 나무가 충분함 -> 높이를 더 높여보자
        result = mid
        start = mid + 1
    else:               # 나무가 부족함 -> 높이를 낮춰야 함
        end = mid - 1

print(result)