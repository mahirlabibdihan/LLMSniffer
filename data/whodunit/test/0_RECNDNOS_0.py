from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = Counter(A)
    max_dishes = max(count.values())
    types = [k for k, v in count.items() if v == max_dishes]
    print(min(types))