import sys

n = int(sys.stdin.readline().rstrip())
time =map(int,sys.stdin.readline().rstrip().split())
re = sorted(time)
answer2 = 0
answer = 0

for i in re:
    answer2 += int(i)
    answer += answer2
print(answer)