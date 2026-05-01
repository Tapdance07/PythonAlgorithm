import sys

while True:
    A,B,C = sys.stdin.readline().rstrip().split()
    if int(B)>17 or int(C)>79:
        print(A +" "+ "Senior")
    elif A=="#" and B=="0" and C=="0":
        break
    else:
        print(A +" " + "Junior")
