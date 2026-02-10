import sys

p, w = map(int, sys.stdin.readline().split())
text = sys.stdin.readline().rstrip()

# 키패드 배열: 인덱스 = 키 번호, 값 = 문자 리스트
keys = [
    ' ',         # 0 (공백)
    '',          # 1 (사용 안 함)
    'ABC',       # 2
    'DEF',       # 3
    'GHI',       # 4
    'JKL',       # 5
    'MNO',       # 6
    'PQRS',      # 7
    'TUV',       # 8
    'WXYZ'       # 9
]

# 문자별 key 번호와 누름 횟수 매핑
char_to_key = {}
for key_num, group in enumerate(keys):
    for i, char in enumerate(group):
        char_to_key[char] = (key_num, i + 1)

result = 0
prev_key = -1

for c in text:
    key, count = char_to_key[c]
    if key == prev_key and key != 0:
        result += w
    result += p * count
    prev_key = key

print(result)
