import sys
A = list()

for _ in range(9):
    A.append(int(sys.stdin.readline().rstrip()))
A.sort()
"""여기까지가 입력받기, 정렬"""

for i in range(9):
    for z in range(9):
        if i == z:
            continue
        else:
            if 100 == sum(A) - A[i] - A[z]:
                for q in range(9):
                    if q==i or q ==z:
                        pass
                    else:
                        print(A[q])
                sys.exit()