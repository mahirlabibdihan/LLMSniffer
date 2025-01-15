from collections import Counter
from math import factorial as f

def nCr(n, r):
    return f(n) // (f(r) * f(n - r))

T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    K = int(input())
    scores.sort(reverse=True)
    max_sum_scores = scores[:K]
    max_score = max_sum_scores[-1]
    total_max_score = scores.count(max_score)
    selected_max_score = max_sum_scores.count(max_score)
    print(nCr(total_max_score, selected_max_score))