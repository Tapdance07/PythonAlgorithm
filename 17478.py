import sys

"""불연속지점을 찾는 게 주된 목적"""
s = sys.stdin.readline().rstrip()

count0 = 0
count1 = 0

if s[0] == '0':
    count0 += 1
else:
    count1 += 1


for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1

# 최소 횟수 출력
print(min(count0, count1))