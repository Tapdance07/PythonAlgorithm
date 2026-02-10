import sys

K,N = map(int,sys.stdin.readline().rstrip().split())

cmlist = list()
for i in range(K):
    cmlist.append(int(sys.stdin.readline().rstrip()))

Start = 1
end = max(cmlist)

while Start <= end:
    mid = (Start + end) //2

    Sum = 0
    for cmble in cmlist:
        Sum += cmble // mid

    if Sum < N:
        end = mid -1
    else:
        Start = mid + 1
print(end)

