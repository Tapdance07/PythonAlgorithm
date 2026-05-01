import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
A_list=list(map(int,sys.stdin.readline().rstrip().split()))

def merge_sort(A):
    