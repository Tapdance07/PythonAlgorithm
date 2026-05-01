import sys

def Factorial(N):
    result = 1
    for i in range(1,N+1):
        result *= i
    return result




N= int(sys.stdin.readline().rstrip())
Test = list(str(Factorial(N)))
Count = 0
for i in range(len(Test)-1,-1,-1):
    if Test[i] =="0":
        Count += 1
    else:
        break
print(Count)