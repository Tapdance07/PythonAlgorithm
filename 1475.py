import sys

num = [0]*10
Count = 0
N = list(map(int,sys.stdin.readline().rstrip()))

for i in range(0,len(N)):
    num[N[i]] += 1

num[6]= num[9] = ( (num[6] + num[9]) //2 +1 if (num[6] + num[9]) %2 >0 else (num[6] + num[9]) //2  )
print(max(num))