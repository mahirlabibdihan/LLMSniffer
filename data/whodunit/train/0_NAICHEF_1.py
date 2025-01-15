from collections import Counter

T = int(input())
for _ in range(T):
    N, A, B = map(int, input().split())
    x = list(map(int, input().split()))
    counts = Counter(x)
    pA = counts[A] / N
    pB = counts[B] / N
    print('{:.15f}'.format(pA * pB))