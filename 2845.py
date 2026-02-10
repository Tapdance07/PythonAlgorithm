import sys

L, P = map(int, sys.stdin.readline().split())
people = L * P
numbers = list(map(int, sys.stdin.readline().split()))
Paper = [x - people for x in numbers]

print(*Paper)
