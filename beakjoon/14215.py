T = list(map(int,input().split()))
while 1:
    if T.count(T[0]) == 3:
        print(T[0]*3)
        break
    else:
        if max(T) >= sum(T) - max(T):
            T[T.index(max(T))] = max(T)-1

        else:
            print(sum(T))
            break