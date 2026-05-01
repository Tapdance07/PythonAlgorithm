import sys

P, K = map(int, sys.stdin.readline().rstrip().split())
i = 2

while i < K:
    if P % i == 0:
        print(f"BAD {i}")
        break
    i += 1
else:
    print("GOOD")
