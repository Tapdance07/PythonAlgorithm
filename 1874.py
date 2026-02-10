import sys

N = int(sys.stdin.readline().rstrip())
waitlist = list()
ans = list()
MaxNum = 0
for i in range(N):
    Num = int(sys.stdin.readline().rstrip())

    if len(waitlist) == 0 and MaxNum==0:
        for i in range(1,Num+1):
            waitlist.append(i)
            ans.append("+")
        MaxNum = waitlist[-1]
    else:
        for i in range(MaxNum+1,Num+1):
            waitlist.append(i)
            ans.append("+")
        if MaxNum < waitlist[-1]:
            MaxNum = waitlist[-1]

    if waitlist[-1] == Num:
        ans.append("-")
        del waitlist[-1]

    elif waitlist[-1] < Num and MaxNum < Num:

        for i in range(MaxNum+1,Num+1):
            waitlist.append(i)
            ans.append("+")
        MaxNum = waitlist[-1]

        if waitlist[-1] == Num:
            ans.append("-")
            del waitlist[-1]


if len(waitlist)>0:
    print("NO")
else:
    for i in ans:
        print(i)





# 1 2 5 7 8 6 3 4

# 1 2 3 4 5 6 7 8

# 4 3 6 8 7 5 2 1

#push , push ,push, push.pop.pop. push.pop,push.push,pop

