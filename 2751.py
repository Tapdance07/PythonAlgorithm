import sys
N = int(sys.stdin.readline().rstrip())
cnt_dic = {}
for _ in range(N):
    X =int(sys.stdin.readline().rstrip())
    if X in cnt_dic:
        cnt_dic[X] += 1
    else:
        cnt_dic[X] = 1
for i in range(max(cnt_dic.keys())+1):
    if i not in cnt_dic:
        continue
    else:
        for _ in range(cnt_dic[i]):
            print(i)