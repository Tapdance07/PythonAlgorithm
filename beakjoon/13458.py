import sys

N = int (sys.stdin.readline().rstrip())
A = list(map(int,sys.stdin.readline().rstrip().split()))
B,C = map(int, sys.stdin.readline().rstrip().split())

"""B는 총감독관이 감시할 수 있는 응시자 수
    C는 부 감독관이 감시할수 있는 응시자 수 
    총감독관은 1명만 가능"""

total = 0

for i in range(N):
    if A[i]-B :

        Sec = A[i]-B
        total += Sec//C
        if Sec%C !=0:
            total +=1

    total += 1
print(total)