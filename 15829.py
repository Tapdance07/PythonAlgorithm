import sys
L = int(sys.stdin.readline().rstrip())

hashing = list(sys.stdin.readline().rstrip())
for i in range(L):

    hashing[i] = (ord(hashing[i]) % 96) * (31 ** i)

print(sum(hashing)%1234567891)