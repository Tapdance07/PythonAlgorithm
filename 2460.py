import sys

train = 0
MaxHuman = 0
for _ in range(10):
    Out,In = map(int,sys.stdin.readline().rstrip().split())
    train += In
    train -= Out
    if MaxHuman < train:
        MaxHuman = train
print(MaxHuman)