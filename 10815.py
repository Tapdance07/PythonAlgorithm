import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

Dict_N = {}
for i in range(N):
    Dict_N[i+1] = sys.stdin.readline().rstrip()

inverted_dict_N = {v: k for k, v in Dict_N.items()}

for i in range(M):
    test = sys.stdin.readline().rstrip()
    if test.isdigit():
        print(Dict_N.get(int(test)))
    else:
        print(inverted_dict_N.get(test))