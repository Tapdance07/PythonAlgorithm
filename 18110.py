import sys

def custom_round(value):

    if value - int(value) >= 0.5:
        return int(value) + 1
    else:
        return int(value)

n = int(sys.stdin.readline().rstrip())

values = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

# 정렬 후 상위 및 하위 15% 제외
exclude_top = custom_round(n * 0.15)
exclude_bottom = n - custom_round(n * 0.15)

filtered_values = sorted(values)[exclude_top:exclude_bottom]

# 평균 계산
if len(filtered_values) == 0:
    print(0)  # 제외 후 값이 없으면 0 출력
else:
    average = sum(filtered_values) / len(filtered_values)
    print(custom_round(average))
