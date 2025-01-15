from collections import Counter

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = Counter(A)
    result = sum(k for k, v in count.items() if v == K)
    print(result if result != 0 else -1)