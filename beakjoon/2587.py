K = []

for i in range(5):
    A = int(input())
    inserted = False


    for z in range(len(K)-1, -1, -1):
        if A > K[z]:
            K.insert(z+1, A)
            inserted = True
            break

    if not inserted:
        K.insert(0, A)

print(sum(K)//len(K))
print(K[len(K)//2])
