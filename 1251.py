import sys

N = sys.stdin.readline().rstrip()
k = len(N)
result = []

for i in range(k - 2):
    for j in range(i + 1, k - 1):
        # Slicing and reversing
        part1 = N[i::-1]
        part2 = N[j:i:-1]
        part3 = N[k - 1:j:-1]


        result.append("".join([part1, part2, part3]))

print(min(result))