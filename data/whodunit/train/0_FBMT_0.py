from collections import Counter

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    goals = [input().strip() for _ in range(n)]
    goal_count = Counter(goals)
    max_goals = max(goal_count.values())
    winners = [team for team, goals in goal_count.items() if goals == max_goals]
    if len(winners) > 1:
        print("Draw")
    else:
        print(winners[0])