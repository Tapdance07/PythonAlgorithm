import sys

# Read number of calls
num_calls = int(sys.stdin.readline().rstrip())

# Read call durations
call_durations = list(map(int, sys.stdin.readline().rstrip().split()))

# Young's plan: every 30 seconds (0~29 -> 1 unit)
def young_plan(calls):
    cost = 0
    for call in calls:
        cost += (call // 30) + 1
    return cost * 10


def min_plan(calls):
    cost = 0
    for call in calls:
        cost += (call // 60) + 1
    return cost * 15


young_cost = young_plan(call_durations)
min_cost = min_plan(call_durations)


if young_cost < min_cost:
    print(f'Y {young_cost}')
elif young_cost > min_cost:
    print(f'M {min_cost}')
else:
    print(f'Y M {young_cost}')
