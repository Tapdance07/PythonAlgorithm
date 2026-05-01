import sys

# 입력 처리
N, M = map(int, sys.stdin.readline().rstrip().split())

# 단어 저장 및 카운트용 딕셔너리
word_count = {}

# 단어 입력
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# 정렬
# 조건: 등장 횟수 내림차순 > 길이 내림차순 > 사전순 오름차순
sorted_words = sorted(
    word_count.items(),
    key=lambda item: (-item[1], -len(item[0]), item[0])
)

# 결과 출력 (단어만 출력)
for word, _ in sorted_words:
    print(word)