import sys

def Fibonacci(n):

    if n == 1:
        return 1
    elif n == 2:
        return  1
    elif n == 0:
        return 0
    else:
      return  Fibonacci(n-1) + Fibonacci(n-2)




N = int(sys.stdin.readline().rstrip())
print(Fibonacci(N))