import sys

T = list(map(int,sys.stdin.readline().rstrip().split()))
i = min(T)
while True:
    c = 0
    i += 1
    for num in T:
        if i % num == 0:
            c +=1
    if c >= 3:
        break
print(i)


