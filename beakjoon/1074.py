# 2ⁿ x 2ⁿ 인 2차원 배열을 Z 모양으로 탐색한다.
import sys

N,r,c = map(int,sys.stdin.readline().rstrip().split())

# 분할정복으로 할때 r이 큰값이면 다 방문하는게 아니라 일부분 자르고 하자
# 한변의 길이 
n2 = 2**N
ans = 0
# 쪼개는 횟수만큼 더하기..

while n2 > 1:
    n2 = n2 // 2
    if r < n2 and c <n2:
        pass
    # 1사분면에 존재할때
    # 여기는 그럼 더 쪼갤수 없으니까 탐색해야지.

    elif r < n2 and c >= n2:
    # 2사분면
    # 여기는 1사분면 만큼한 늘려주면 될걸
        ans += n2 *n2 * 1
        c -= n2

    elif r >= n2 and c < n2:
        ans += n2 * n2 * 2
        r -= n2
    # 3사분면
    # 여기는 1,2, 사분면 만큼의 횟수 늘려줘
        

    elif r >= n2 and c >= n2:
    # 4사분면
    # 여기는 1,2,3,사분면의 크기만큼 늘려
        ans += n2 * n2 * 3
        c -= n2
        r -= n2

print(ans)