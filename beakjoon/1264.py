while True:
    A = list(input())
    alp = ['a', 'e', 'i', 'o', 'u']
    upalp = ['A','E','I','O','U']
    if A[0] == '#':
        break
    else:
        result = 0

        for i in range(len(A)):
            if A[i] in alp or A[i] in upalp:

                result += 1

        print(result)
