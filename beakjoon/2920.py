import sys

sing = list(map(int,sys.stdin.readline().rstrip().split()))

if sing == list(range(1, 9)):
    print('ascending')
elif sing == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')
