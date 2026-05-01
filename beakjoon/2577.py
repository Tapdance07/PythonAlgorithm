import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

strlist = list(str(A*B*C))
countlist = [0]*10
for i in range(len(strlist)):
    countlist[int(strlist[i])] += 1

for i in countlist:
    print(i)