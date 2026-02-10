import sys

Time = list(map(int,sys.stdin.readline().rstrip().split()))
BakeTime = int(sys.stdin.readline().rstrip())
HH = BakeTime // (60*60)
MM = (BakeTime % 3600) // 60
SS = BakeTime % 60

Time[0] += HH
Time[1] += MM
Time[2] += SS

if Time[2]>=60:
    Time[1] += (Time[2]//60)
    Time[2] = Time[2]%60
if Time[1]>=60:
    Time[0] += (Time[1]//60)
    Time[1] = Time[1]%60
if Time[0]>=24:
    Time[0] = Time[0]%24
print(*Time)