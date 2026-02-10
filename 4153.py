import sys

while True:
    triagle = list(map(int,sys.stdin.readline().rstrip().split()))
    triagle.sort()
    if sum(triagle) == 0:
        break
    else:
        print('right' if triagle[0]**2 + triagle[1]**2 == triagle[2]**2 else 'wrong')