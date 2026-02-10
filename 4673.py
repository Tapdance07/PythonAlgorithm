B = set()

for i in range(1, 10001):
    generated = i + sum(map(int, str(i)))
    B.add(generated)

for i in range(1, 10001):
    if i not in B:
        print(i)