import sys

N = int(sys.stdin.readline().rstrip())
shirt = list(map(int,sys.stdin.readline().rstrip().split()))
T,P = map(int,sys.stdin.readline().rstrip().split())

Count = 0
for i in range(len(shirt)):

    if shirt[i]//T == 0 and shirt[i] != 0:
        Count += 1
    else:
        if shirt[i]%T != 0:
            Count += shirt[i] // T + 1
        else:
            Count += shirt[i] // T
print(Count)
print(f'{N//P} {N % P}')
