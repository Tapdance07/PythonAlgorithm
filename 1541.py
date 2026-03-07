# 양수와 +, -, 괄호를 가지고 식을 만들었다.
# 괄호를 모두 지운 식을 주었을때
# 괄호를 적절히 쳐서 이식의 값을 최소로 만들려고 한다.
# 입력으로 식이 주어진다.
import sys
input_data = sys.stdin.readline().rstrip().split('-')

result = 0

# -가 나오기 전까지의 값들은 합치고
first_group = input_data[0].split('+')
for num in first_group:
    result += int(num)

# -가 나온 이후의 값들은 괄호를 치면 어떻게든 마이너스로 바꿀수 있기때문에
# 모두 더해서 첫번째 그룹의 값에서 뺀다.
for group in input_data[1:]:
    sub_sum = sum(map(int, group.split('+')))
    result -= sub_sum

print(result)