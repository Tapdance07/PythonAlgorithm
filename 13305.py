# 어떤 나라에 N개의 도시가 있다.
# 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차를 이용하여 이동하려고 한다.
# 도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다.
# 각 도시 사이에는 도로가 있고, 각 도로의 길이는 다를 수 있다.
# 각 도시에서는 기름을 살 수 있다. 각 도시에서 1리터의 기름을 사는 가격이 다를 수 있다.
# 자동차의 연료 탱크는 무한이므로, 필요한 만큼 기름을 사서 이동할 수 있다.
# 예를 들어, 4개의 도시가 있고, 각 도시에서 1리터의 기름을 사는 가격이 각각 5, 2, 4, 1이라고 하자.
# 가장 적은 비용으로 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다.

N = int(input())
distances = list(map(int,input().split()))
costs = list(map(int,input().split()))

# 그리드 알고리즘을 이용하여 문제를 해결하면 될것 같다.

total_cost = 0
current_cost = costs[0]
for i in range(N-1):
    if costs[i] < current_cost:
        current_cost = costs[i]
        total_cost += current_cost * distances[i]
    else:
        total_cost += current_cost * distances[i]
print(total_cost)