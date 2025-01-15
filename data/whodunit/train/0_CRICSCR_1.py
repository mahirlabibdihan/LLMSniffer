def is_valid_scorecard(n, scores):
    runs, wickets = zip(*scores)
    if runs != tuple(sorted(runs)) or wickets != tuple(sorted(wickets)) or max(wickets) > 10:
        return "NO"
    return "YES"

n = int(input().strip())
scores = []
for _ in range(n):
    r, w = map(int, input().strip().split())
    scores.append((r, w))

print(is_valid_scorecard(n, scores))