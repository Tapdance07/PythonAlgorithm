# N+1개의 I와 N개의 O로 아루어져 있으면 I와 o이 교대로 나오는 문자열을 Pn이라고 한다.
# p1 ioi
# p2 ioioi
# p3 ioioioi
# i와 O로만 이루어진 문자열 s와 정수 N이 주어졌을 때 S안에 Pn이 몇군데 포함되어 있는지
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

# 여기까지가 기초세팅 받기 
count = 0
# 이거는 IOI를 세기 위함이다. 이걸 최종 출력하면 될것 같다.
ioicheck = 0
index = 0

while index < (M - 2):
    # 'IOI' 패턴을 발견하면
    if S[index:index+3] == "IOI":
        ioicheck += 1
        # 만약 IOI가 N번 연속되었다면 Pn을 찾은 것!
        if ioicheck == N:
            count += 1
            # 찾은 후 ioicheck를 0으로 만들지 않고 1을 빼줌으로써
            # 바로 다음에 이어지는 IOI와 겹치는 부분을 계산함 (IOIOI 패턴 처리)
            ioicheck -= 1
        
        index += 2 # IOI를 확인했으니 2칸 점프
    else:
        # 패턴이 깨지면 연속 횟수 초기화
        ioicheck = 0
        index += 1

print(count)

    