import sys
day = {0:"SUN",1:"MON",2:"TUE",3:"WED",4:"THU",5:"FRI",6:"SAT"}
x,y = map(int,sys.stdin.readline().split())
c = y
for A in range(1,x):
    if A==4 or A==6 or A==9 or A==11:
        b = 30
    elif A == 2:
        b = 28
    else:
        b = 31
    c += b
print(day[c%7])
