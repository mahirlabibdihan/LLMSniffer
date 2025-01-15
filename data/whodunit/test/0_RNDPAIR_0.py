T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    max_val = max(A)
    max_count = A.count(max_val)
    if max_count > 1:
        print(1)
    else:
        second_max = sorted(A)[-2]
        second_max_count = A.count(second_max)
        print(second_max_count / (N * (N - 1) / 2))