import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
#N 이상 M 이하의 소수 판별하기

array = [True]* (M+1)
array[0] = array[1] = False
for i in range(2,int(M**0.5)+1):
    if array[i]:
        j = 2
        while i * j <= M:
            array[i * j] = False
            j += 1

for i in range(N,M+1):
    if array[i]:
        print(i)