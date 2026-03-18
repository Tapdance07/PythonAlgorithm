# 정사각형의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 연결된건 좌우 위아래로 다른집이 있는 경우를 말함
# 대각선은 미포함한다.
# 각 단지에 속하는 집의 수를 오름차순으로 정렬한다.

import sys

N = int(sys.stdin.readline().rstrip())
apt = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(N)]

from collections import deque

# 일단