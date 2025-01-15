T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    coins = list(input().split())
    for i in range(K):
        if coins.pop() == 'H':
            coins = ['H' if c == 'T' else 'T' for c in coins]
    print(coins.count('H'))