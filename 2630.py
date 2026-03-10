# 정사각형 칸들로 이루어진 정사각형 모양의 종이가 주어져있고, 각 정사각형들은 하얀색으로 
# 칠해져 있거나 파란색으로 칠해져 있다. 
# 전체 종이의 크기가 N*N 이라면 종이를 자르는 규칙은 다음과 같다.
# 전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서
# 똑같은 크기의 네개의 N/2 * n/2 크기로 나눈다.
# 또한 잘라진 사각형에 모두 하얀색 또는 모두 파란색이나 하나의 정사각형 칸이 되어 더이상 
# 자를수 없을 때까지 반복한다.
# N이 주어지는데 N은 2, 4, 8, 16, 32, 64, 128중 하나이다

import sys
N = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 리스트 컴프리헨션으로 한줄로 이중 리스트 만들기

white = 0
blue = 0
# 흰색과 파란색의 종이의 갯수 세기

def cut(x,y,n):
    global white, blue
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1
cut(0,0,N)
print(white)
print(blue)