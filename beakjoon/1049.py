# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고,
# 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의가 격, 낱개로 살 때의 가격이 주어질 때,
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램

N, M = map(int,input().split())
min_set_price = float('inf')
min_solo_price = float('inf')
set_count = N // 6 + 1
for _ in range(M):

    set_price, solo_price = map(int,input().split())
    # 패키지의 가격이 낱개의 6배의 가격보다 저렴한 경우를 판단한다.
    # min_price = min(min_price, set_price * set_count, solo_price * N)
    # 처음에는 이렇게 생각했ㄲ는데 이렇게 하는게 아니라 
    # 패키지와 낱개를 섞어서 사는 경우도 가능하구나?
    # 그럼 가장 편하게 패키지의 최소 가격과 낱개의 최소가격으로 계산하면 되는거 아닌가?
    min_set_price = min(min_set_price, set_price)
    min_solo_price = min(min_solo_price, solo_price)

case1 = ((N // 6) + 1) * min_set_price

# 전부 낱개로 살 때
case2 = N * min_solo_price

# 섞어서 살 때 (6개 묶음은 패키지로, 나머지는 낱개로)
case3 = (N // 6) * min_set_price + (N % 6) * min_solo_price

# 세 경우 중 최솟값 출력
print(min(case1, case2, case3))