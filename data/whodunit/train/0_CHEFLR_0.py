T = int(input().strip())
MOD = 10**9 + 7
for _ in range(T):
    S = input().strip()
    ans = 1
    for i in range(len(S)):
        if S[i] == 'l':
            ans = (ans*2) % MOD
        else:
            ans = (ans*2 + 2) % MOD
    print(ans)