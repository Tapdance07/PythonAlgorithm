import sys

while True:
    T = int(sys.stdin.readline().rstrip())
    if T==0:
        break
    result = 2
    Size = len(str(T))
    result += Size - 1
    for i in range(Size):
        if str(T)[i]=='1':
            result += 2
        elif str(T)[i]=='0':
            result += 4
        else:
            result += 3
    print(result)