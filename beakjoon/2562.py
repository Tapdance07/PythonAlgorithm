A = [0] * 9
M = 0
C = 0
for i in range(9):
    A[i] = int(input())
    if i == 0:
        M = A[i]
        C = 1
    else:
        if M < A[i]:
            M = A[i]
            C = i+1
        else:
            pass
print(M)
print(C)