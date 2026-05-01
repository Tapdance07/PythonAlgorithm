import sys

Taro = 1000 - int(sys.stdin.readline().rstrip())
"""1000엔에서 taro값을 뺀걸 500, 100, 50, 10, 5, 1엔으로
    나눠서 줘야한다. 최소 갯수의 지폐를 사용하는 수"""

result = 0
Money = [500,100,50,10,5,1]
for i in range(len(Money)):
    rep = Taro // Money[i]
    result += rep
    Taro -= rep * Money[i]
print(result)