def max_goal_diff(T, test_cases):
    for _ in range(T):
        N, goals = test_cases[_]
        min_goals = goals[0]
        max_diff = goals[1] - goals[0]
        for i in range(1, N):
            max_diff = max(max_diff, goals[i] - min_goals)
            min_goals = min(min_goals, goals[i])
        if max_diff <= 0:
            print("UNFIT")
        else:
            print(max_diff)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    goals = list(map(int, input().split()))
    test_cases.append((N, goals))
max_goal_diff(T, test_cases)