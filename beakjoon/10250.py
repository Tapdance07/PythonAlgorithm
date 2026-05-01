import sys

T = int(sys.stdin.readline().rstrip())  # 테스트 케이스 개수 입력

for _ in range(T):
    H, W, X = map(int, sys.stdin.readline().rstrip().split())
    # 층수와 방 번호 계산
    floor = (X - 1) % H + 1
    room = (X - 1) // H + 1
    # 출력 형식: 층수 + 방 번호(두 자리)
    print(f"{floor}{room:02}")