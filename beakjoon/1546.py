N = int(input())

abc = list(map(int, input().split()))
Mx =  max(abc)
for i in range(N):
    abc[i] = abc[i] / Mx  * 100

print(sum(abc)/N)