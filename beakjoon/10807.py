#
# N = int(input())
#
# for i in range(N):
#     print(" "*(N-(i+1)) + "*"*(i+1))

#
# N = int(input())
# A = list(map(int,input().split()))
# v = int(input())
#
# print(A.count(v))

N, X = map(int,input().split())
A = list(map(int,input().split()))
# A = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]


for i in range(len(A)):
    if A[i] < X:
       print(A[i] , end = ' ')











