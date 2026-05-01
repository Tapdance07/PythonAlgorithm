T = int(input())
for _ in range(T):
    input()  # 빈 줄 무시용 (혹시 있을 경우 대비)
    N, M = map(int, input().split())
    sejun = list(map(int, input().split()))
    sebi = list(map(int, input().split()))

    max_sejun = max(sejun)
    max_sebi = max(sebi)

    if max_sejun > max_sebi:
        print('S')
    elif max_sejun < max_sebi:
        print('B')
    else:
        print('C')
