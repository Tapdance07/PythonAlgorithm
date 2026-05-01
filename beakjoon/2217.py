# N의 로프가 주어진다.
# 각 로프마다 버틸 수 있는 최대 중량이 다르다.
# 이때, 로프를 여러 개 연결하여 사용할 때 최대 중량을 구하는 프로그램을 작성하시오.
N = int(input())
ropes = [int(input()) for _ in range(N)]
# 로프에 균일하게 w/n 만큼의 무게가 걸린다.
# 로프는 임의로 몇개의 로프만 골라서 사용해도 무방하다.
ropes.sort(reverse=True) # 내림차순 정렬
max_weight = 0
for i in range(N):
    weight = ropes[i] * (i + 1) # i+1개의 로프를 사용할 때의 최대 중량
    max_weight = max(max_weight, weight) # 최대 중량 갱신
print(max_weight)