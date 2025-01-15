MOD = 10**9 + 7
for _ in range(int(input().strip())):
    S = input().strip()
    ans = 1
    for i, s in enumerate(S):
        ans = (ans*2 + int(s == 'r')*2) % MOD
    print(ans)