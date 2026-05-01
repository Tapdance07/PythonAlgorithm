A =list()
for i in range(5):
    A.append(list(input()))
try:
    for z in range(15):
        for i in range(5):
            if (i!=4) and (len(A[i]) <= z ):
                pass
            else:
                print(A[i][z],end='')
except:
    i += 1

