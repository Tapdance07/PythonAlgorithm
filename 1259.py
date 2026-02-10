import sys

while True:
    T = list(sys.stdin.readline().rstrip())
    if T[0] == "0":
        break
    else:
        ans = 'yes'
        for i in range(len(T)//2):
            if T[i] == T[-i-1]:
                pass
            else:
                ans = 'no'
                break
        print(ans)