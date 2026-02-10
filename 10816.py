import sys

N = int(sys.stdin.readline().rstrip())
NT = list(map(int,sys.stdin.readline().rstrip().split()))


M = int(sys.stdin.readline().rstrip())
MT = list(map(int,sys.stdin.readline().rstrip().split()))


#NT에 있는 걸 숫자를 카운팅 해서 카운팅 딕셔너리로 만들고 그걸 MT와 비교
NT_Dict = {}
for i in range(N):
    if NT[i] not in NT_Dict:
        NT_Dict[NT[i]] = 1
    else:
        NT_Dict[NT[i]] = int(NT_Dict[NT[i]]) + 1

for i in MT:
    print(NT_Dict.get(i, 0), end=" ")

