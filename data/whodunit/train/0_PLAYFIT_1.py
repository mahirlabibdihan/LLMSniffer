def max_goal_diff(T, test_cases):
    for _ in range(T):
        N, goals = test_cases[_]
        min_goals = [0]*N
        min_goals[0] = goals[0]
        for i in range(1, N):
            min_goals[i] = min(min_goals[i-1], goals[i])
        max_diff = max([j-i for i, j in zip(min_goals, goals)])
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