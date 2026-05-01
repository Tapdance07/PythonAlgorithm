T = int(input())  # 입력 횟수
K = []  # 정렬된 리스트

for i in range(T):
    A = int(input())  # 새로운 값 입력
    inserted = False  # 삽입 여부 확인

    # 리스트를 역순으로 탐색하여 올바른 위치에 삽입
    for z in range(len(K)-1, -1, -1):
        if A > K[z]:
            K.insert(z+1, A)  # 적절한 위치에 삽입
            inserted = True
            break

    if not inserted:  # 리스트의 모든 값보다 작으면 맨 앞에 삽입
        K.insert(0, A)

for i in K:
    print(i)
