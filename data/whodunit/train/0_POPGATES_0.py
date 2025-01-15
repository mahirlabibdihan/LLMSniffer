T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    coins = list(input().split())
    heads = 0
    for i in range(N-1, N-K-1, -1):
        if coins[i] == 'H':
            heads += 1
            for j in range(i):
                if coins[j] == 'H':
                    coins[j] = 'T'
                else:
                    coins[j] = 'H'
    print(coins.count('H'))