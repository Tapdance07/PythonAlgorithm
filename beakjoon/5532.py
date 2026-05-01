L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A%C != 0:
    LA = (A//C) + 1
else:
    LA = (A//C)
if B%D != 0:
    LB = (B//D) + 1
else:
    LB = (B//D)
print(L-max([LA,LB]))
