T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    min_diff = float('inf')
    for i in range(1, N):
        min_diff = min(min_diff, coins[i] - coins[i-1])
    print(min_diff)