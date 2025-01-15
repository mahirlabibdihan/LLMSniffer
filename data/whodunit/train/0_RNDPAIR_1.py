T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    max_val = max(A)
    max_count = A.count(max_val)
    if max_count > 1:
        print(1)
    else:
        second_max = None
        for i in A:
            if i != max_val and (second_max is None or i > second_max):
                second_max = i
        second_max_count = A.count(second_max)
        print(second_max_count / (N * (N - 1) / 2))