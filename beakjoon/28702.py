import sys

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
third = sys.stdin.readline().rstrip()

intAns = 0
if str.isdigit(first):
        intAns = int(first) + 3
elif str.isdigit(second):
        intAns = int(second) + 2
elif str.isdigit(third):
        intAns = int(third) + 1

if intAns %3 == 0 and intAns%5 == 0:
        print('FizzBuzz')
elif intAns %3 ==0 and intAns%5 != 0:
        print('Fizz')
elif intAns % 3 != 0 and intAns % 5 == 0:
        print('Buzz')
else:
        print(intAns)