import sys

N = int(sys.stdin.readline().rstrip())

Li = list(map(int, sys.stdin.readline().rstrip().split()))

Stack = []
Snack = []
i = 1  # 넘겨야 하는 숫자

while True:
    if len(Li) > 0 and Li[0] == i:
        Snack.append(Li.pop(0))
        i += 1

    elif len(Stack) > 0 and Stack[-1] == i:
        Snack.append(Stack.pop())
        i += 1

    elif len(Li) > 0:

        Stack.append(Li.pop(0))

    else:

        break
if Snack == list(range(1, N + 1)):
    print("Nice")
else:
    print("Sad")