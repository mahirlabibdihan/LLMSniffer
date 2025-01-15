T = int(input())
for _ in range(T):
    n = int(input())
    stems = list(map(int, input().split()))
    required = list(map(int, input().split()))
    if sum(stems) != sum(required) or min(required) < 0:
        print(-1)
    else:
        diff = [stems[i] - required[i] for i in range(n)]
        print(sum([i for i in diff if i > 0]))