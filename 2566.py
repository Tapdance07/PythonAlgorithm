A =list()
mx = 0
y = 0
x = 0
for i in range(9):
    A.append(list(map(int,input().split())))

    if mx != max(map(max, A)):
        mx = max(map(max, A))
        y = A[i].index(mx)
        x = i
print(mx)
print(x+1,y+1)