import sys

A,B = map(int,sys.stdin.readline().rstrip().split())

if A == B:
    print(B-A)
    print(*(list(range(A + 1, B, 1))))
elif A<B:
    print(B-A-1)
    print(*(list(range(A + 1, B, 1))))
else:
    print(A-B-1)
    print(*(list(range(B + 1, A, 1))))
