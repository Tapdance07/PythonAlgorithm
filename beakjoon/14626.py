# ISBN에는 국가명, 발행자 등의 정보가 담겨 있으며 13자리의 숫자로 표시된다.
# 마지막 숫자는 체크기호로 ISBN의 정확성 여부를 점거할 수 있는 숫자이다.
# 체크기호는 일련번호의 앞에수버투 각 자리마다 가중치 1,3,1,3, 를 곱한 것을 모두 더하고 
# 그 값을 10으로 나눈 나머지가 0이 되도록 만드는 숫자 m을 사용한다 

import sys

N = list(sys.stdin.readline().rstrip())

total_sum = 0
star_index = -1

for i in range(len(N)):
    if N[i] == '*':
        star_index = i
        continue
    
    # 숫자 변환
    num = int(N[i])
    
    if i % 2 == 0:
        total_sum += num * 1
    else:
        total_sum += num * 3

# (합계 + (별표자리 숫자 * 가중치)) % 10 == 0 이 되는 숫자 찾기
weight = 1 if star_index % 2 == 0 else 3

for m in range(10):
    if (total_sum + (m * weight)) % 10 == 0:
        print(m)
        break