import sys

#덩치는 키도 커야하고 몸무게도 많이 나가야 함

T = int(sys.stdin.readline().rstrip())

WHRank = list()
for i in range(T):
    x,y = map(int,sys.stdin.readline().rstrip().split())
    a =(x,y)
    WHRank.append(a)

ranks = []
for i in range(T):
    rank = 1
    for j in range(T):
        if i != j and WHRank[i][0] < WHRank[j][0] and WHRank[i][1] < WHRank[j][1]:
            rank += 1
    ranks.append(rank)


print(" ".join(map(str, ranks)))