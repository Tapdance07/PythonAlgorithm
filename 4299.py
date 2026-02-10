import sys

A,B = map(int,sys.stdin.readline().rstrip().split())
if A > B :
    TB = (A-B)/2
    TA = A - TB
    print(int(TA), int(TB))
else:
    print(-1)