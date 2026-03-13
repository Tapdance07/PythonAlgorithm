# 대학의 캠퍼스는 N * M 크기이다.
# 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
# 예를 들어 (x,y) 에 있다면 이동할 수있는 곳은 (x +1,y), (x -1,y), (x,y +1), (x,y -1) 이다.
# 캠퍼스에서 만날 수 있는 사람의 수를 출력
import sys

N,M = map(int, sys.stdin.readline().rstrip().split())