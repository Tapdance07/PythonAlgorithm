import sys

# 입력 받기
N = int(sys.stdin.readline().rstrip())
T = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


mean = round(sum(T) / N)


T.sort()
median = T[N // 2]


frequency = {}
for num in T:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_count = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_count]
modes.sort()

if len(modes) > 1:
    mode = modes[1]
else:
    mode = modes[0]


range_value = max(T) - min(T)


print(mean)
print(median)
print(mode)
print(range_value)
