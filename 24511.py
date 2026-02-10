import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
DataCon = list(map(int,sys.stdin.readline().rstrip().split()))
Datalist = deque()
Datalist.extend(map(int,sys.stdin.readline().rstrip().split()))
Data_N = int(sys.stdin.readline().rstrip())
input_Data = list(map(int,sys.stdin.readline().rstrip().split()))
# Datalist.extendleft(input_Data)
ans = list()

#선입 선출인 DataCon이 0인 애들만 확인하면 되는데
for i in range(N):
    if Data_N > len(ans):
     if DataCon[-i-1] == 0:
        ans.append(Datalist[-i-1])
    else:
        break

if len(ans)<Data_N:
    for i in range(Data_N-len(ans)):
        ans.append(input_Data[i])

print(*ans)














# for i in range(Data_N):
#     first_input_Data = input_Data[i]
#     for z in range(N):
#
# #Data_N 이 0이면 큐 , 1 이면 스택
# #큐는 선입 선출, 스택은 선입 후출
#         if DataCon[z] == 0:
#             pop_data = Datalist[z]
#             Datalist[z] = first_input_Data
#             first_input_Data = pop_data
#         else:
#             pass
#     ans.append(first_input_Data)
# print(*ans)

#for 문이 두개라 1초 시간 제한에 걸림
#이중 반복문의 경우 시간복잡도가 n^2이기에 반복문은 1개만 사용하거나 log2로 진행해야함