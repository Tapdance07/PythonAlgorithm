import sys

N = int(sys.stdin.readline().rstrip())
result = list(sys.stdin.readline().rstrip())
for _ in range(N-1):
    B = sys.stdin.readline().rstrip()
    for i in range(len(result)):
        if result[i] != B[i]:
            result[i] = "?"
print("".join(result))