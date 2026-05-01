A = []
C = 0
for i in range(10):
    A.append(int(input())%42)
    if A[i] not in A[:i]:
        C += 1

print(C)

