import sys

#팰린드롬이면 1, 아니면 0

def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt + 1
    elif s[l] != s[r]:
        return 0, cnt + 1
    else:
        return recursion(s, l + 1, r - 1, cnt + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    print(*isPalindrome(sys.stdin.readline().rstrip()))
