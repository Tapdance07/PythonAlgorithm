import sys

#MA에 있는 수가 A에 있는 지 확인




N = int(sys.stdin.readline().rstrip())

A = set(map(int,sys.stdin.readline().rstrip().split()))

M =  int(sys.stdin.readline().rstrip())

MA = list(map(int,sys.stdin.readline().rstrip().split()))


for i in MA:
    if i in A:
        print(1)
    else:
        print(0)

