N = int(input())
A = list(map(int,input().split()))
Coun = 0
for i in range(N):
    if A[i] == 1:
        continue

    for j in range(2, A[i]):
        if A[i]%j == 0:
            break
    else:
        Coun +=1

print(Coun)
