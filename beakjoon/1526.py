import sys



def is_geumminsu(num):
    return all(ch in '47' for ch in str(num))

def find_largest_geumminsu(N):
    for num in range(N, 3, -1):  # 4보다 크거나 같은 수만 고려
        if is_geumminsu(num):
            return num

# 입력
N = int(sys.stdin.readline().rstrip())

# 출력
print(find_largest_geumminsu(N))
