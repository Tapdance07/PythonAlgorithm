# 절댓값 힙은 다음과 같은 연산을 지원한다
# 배열에 정수 x를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
# 절댓값이 가장 작은 값이 여러개일 때는 가장 작은 수를 출력하고 그 값을 배열에서 제거한다.

import sys
N = int(sys.stdin.readline().rstrip())

x = int(sys.stdin.readline().rstrip())
import heapq
