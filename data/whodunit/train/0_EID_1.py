T = int(input())
for _ in range(T):
    N = int(input())
    coins = sorted(map(int, input().split()))
    min_diff = min(b-a for a, b in zip(coins, coins[1:]))
    print(min_diff)