MOD = 10**9 + 7

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = list(map(int, input().split()))
        S.sort()
        power_of_two = [1]
        for i in range(1, N):
            power_of_two.append((power_of_two[-1]*2) % MOD)
        ans = 0
        for i in range(N):
            ans = (ans + (S[i] * (power_of_two[i] - power_of_two[N-i-1])) % MOD) % MOD
        print(ans)

solve()