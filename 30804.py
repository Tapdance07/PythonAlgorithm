# N개의 과일이 꽂혀있는 과일 탕후루
# 과일의 종류에는 1부터 9까지 번호가 붙어있다.
# 과일 탕후루를 만들었지만 과일을 두 종류 이하로 사용해달라는 것이다
# 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기로 하였다.
# 앞에서 a개,뒤에서 b개의 과일을 빼면 총 N - (a+b)개의 과일이 있는 탕후루
# 과일의 개수가 제일 많은 탕후루의 과일 개수

import sys

N = int(sys.stdin.readline().rstrip())
fruits = list(map(int,sys.stdin.readline().rstrip().split()))
# 과일을 입력 받아
# 두 포인트와 브루트 포스를 둘 다 적용을 해야한다.
# 이렇게 되면 결국엔 set을 해서 크기가 2일때까지 반복하는 것을 만드는 것이 
# 최선의 알고리즘이지 않을까?
# 무언가의 행동을 하기 전에 set(fruits)를 통해서 2보다 작은지를 학인한다.
count_list = [0] * 10
left = 0
max_fruits = 0
kind = 0 

for right in range(N):
    target_fruit = fruits[right]
    
    if count_list[target_fruit] == 0:
        kind += 1
        
    count_list[target_fruit] += 1
    
    while kind > 2:
        left_fruit = fruits[left]
        count_list[left_fruit] -= 1
        
        if count_list[left_fruit] == 0:
            kind -= 1
        
        left += 1
    
    current_len = right - left + 1
    if current_len > max_fruits:
        max_fruits = current_len

print(max_fruits)
