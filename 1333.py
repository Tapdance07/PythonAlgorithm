import sys

N, L, D = map(int, sys.stdin.readline().split())

# 전체 앨범 재생 시간
album_time = N * L + (N - 1) * 5

# 전화벨은 D초마다 1초간 울림
ring = 0
while True:
    if ring > album_time:
        # 벨이 울린 시간이 앨범 전체 끝난 이후라면 그냥 출력
        print(ring)
        break

    # 곡과 공백 사이 순회
    for i in range(N):
        start = i * (L + 5)         # 각 곡 시작 시간
        end = start + L             # 곡이 끝나는 시간
        gap_end = end + 5           # 공백이 끝나는 시간

        if end <= ring < gap_end:
            print(ring)
            sys.exit()

    # 다음 전화벨 시간
    ring += D
