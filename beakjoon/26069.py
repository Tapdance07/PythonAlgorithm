import sys

#ChongChong이와 만난 사람들이 점차 무지개 댄스를 추는 것


N = int(sys.stdin.readline().rstrip())

RainbowDance = set()
RainbowDance.add("ChongChong")

for i in range(N):
    A, B = sys.stdin.readline().rstrip().split()
    if A in RainbowDance or B in RainbowDance:
        RainbowDance.add(A)
        RainbowDance.add(B)

print(len(RainbowDance))


