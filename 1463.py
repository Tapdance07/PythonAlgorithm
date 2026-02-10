import sys

# 1 <= N <= 10**6
N = int(sys.stdin.readline().rstrip())
Count = 0
while N != 1:
    print(N)
    if N % 2 ==0 or N % 3 == 0:
        if N % 3 == 0:
            if (N-1)// 2 < N//3:
                N = (N-1) // 2
                Count += 2
            else:
                N //= 3
                Count += 1
        else:
            if (N-1)// 3 < N//2:
                N = (N-1) // 3
                Count += 2
            else:
                N //= 2
                Count += 1
    else:
        N -= 1
        Count += 1
print(Count)
