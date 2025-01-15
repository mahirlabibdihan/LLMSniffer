def is_valid_scorecard(n, scores):
    for i in range(1, n):
        if scores[i][0] < scores[i-1][0] or scores[i][1] < scores[i-1][1] or scores[i][1] > 10:
            return "NO"
    return "YES"

n = int(input().strip())
scores = []
for _ in range(n):
    r, w = map(int, input().strip().split())
    scores.append((r, w))

print(is_valid_scorecard(n, scores))