# AC는 정수 배열에 연산을 하기 위해 만든 언어이다.
# 이 언어네느 두가지 함수 R 과 D가 있다.
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고
# 함수 D는 첫번째 수를 버리는 함이다.
# 배열이 비어있는 D를 사용한 경우네느 에러가 발생한다.

import sys
from collections import deque

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    p = input().rstrip()  
    n = int(input().rstrip())  
    strparse = input().rstrip()  
    
    if strparse == "[]":
        name = deque()
    else:
        name = deque(map(int, strparse.strip('[]').split(',')))
    
    rev_flag = False  
    is_error = False  
    
    for cmd in p:
        if cmd == 'R':
            # 실제로 뒤집지 않고 상태만 반전시킴 
            rev_flag = not rev_flag
        elif cmd == 'D':
            if not name:
                is_error = True
                break
            
            if rev_flag:
                name.pop()      # 뒤집힌 상태면 뒤에서 제거
            else:
                name.popleft()  # 정방향 상태면 앞에서 제거


    if is_error:
        print("error")
    else:
        # 마지막에 rev_flag가 True라면 실제로 한 번 뒤집어줌
        if rev_flag:
            name.reverse()
        
        # 출력 형식을 [1,2,3] 형태로 맞춰줌
        print("[" + ",".join(map(str, name)) + "]")