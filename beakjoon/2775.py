import sys

T= int(sys.stdin.readline().rstrip())

def human (a,b):
    pass




for i in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    Sum = list(range(1,n+1))
    for z in range(k):
        for p in range(n):
            if p == 0:
                pass
            else:
                Sum[p] = Sum[p-1]+ Sum[p]
    print(Sum[-1])


#1층은 sum(list(range(1,b+1))

#1  5  15 35 70 126
#1  4  10 20 35 56
#1  3  6  10 15 21
#1  2  3  4  5  6