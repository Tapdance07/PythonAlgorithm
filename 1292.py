import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

sequence = []
num = 1


while len(sequence) < B:
    sequence += [num] * num
    num += 1

print(sum(sequence[A-1:B]))