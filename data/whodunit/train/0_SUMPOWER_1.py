T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    S = input().strip()
    power = sum(len(set(S[i:i+K])) - 1 for i in range(N-K+1))
    print(power)