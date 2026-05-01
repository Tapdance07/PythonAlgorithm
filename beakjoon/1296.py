def calculate_compatibility(base_name, team_name):
    # L, O, V, E 개수 세기
    L = O = V = E = 0
    combined = base_name + team_name
    for ch in combined:
        if ch == 'L':
            L += 1
        elif ch == 'O':
            O += 1
        elif ch == 'V':
            V += 1
        elif ch == 'E':
            E += 1
    # 공식에 따라 궁합 계산
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100


# 입력 받기
yeondu_name = input().strip()
n = int(input().strip())
team_names = [input().strip() for _ in range(n)]

# 가장 높은 확률과 가장 좋은 팀 이름 저장 변수
best_team = ""
best_score = -1

# 모든 팀 이름에 대해 궁합 점수 계산
for team in team_names:
    score = calculate_compatibility(yeondu_name, team)
    if score > best_score:
        best_score = score
        best_team = team
    elif score == best_score:
        # 같은 점수면 사전순으로 앞선 팀을 선택
        if team < best_team:
            best_team = team

# 결과 출력
print(best_team)
