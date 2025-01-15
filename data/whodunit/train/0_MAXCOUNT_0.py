from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count_dict = Counter(A)
    max_count = max(count_dict.values())
    max_elements = [k for k, v in count_dict.items() if v == max_count]
    print(min(max_elements), max_count)