import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
CoiniList = list()

for i in range(N):
    CoiniList.append(int(sys.stdin.readline().rstrip()))

#최대 사이즈 찾기
CoiniList.reverse()
Coin = 0
for i in range(N):
    Coin += (K//CoiniList[i])
    K %= CoiniList[i]
    if K == 0:
        break

print(Coin)
